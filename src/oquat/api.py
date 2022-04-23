import json.decoder
import random
import sys
from collections import defaultdict
from dataclasses import dataclass
from operator import itemgetter
from pathlib import Path
from typing import Optional

import bioregistry
import click
import pystow
import requests
from more_click import verbose_option
from tabulate import tabulate
import re
from .robot import robot_parse_json_local, robot_parse_json_remote
from .struct.obograph import Graph, Graphs


@dataclass
class Results:
    """A package of assessment results."""
    versions: dict[str, Optional[str]]
    unknown_prefixes: dict[str, dict[str, str]]
    noncanonical_prefixes: dict[str, dict[str, str]]
    malformed_curies: dict[str, set[str]]
    invalid_luids: dict[str, set[str]]

    def _malformed_curies_table(self):
        bvi = [(k, v) for k, values in sorted(self.malformed_curies.items()) for v in sorted(values)]
        return tabulate(bvi, headers=["node_id", "xref"], tablefmt="github")

    def _bad_values_md(self):
        return f"""
## Invalid CURIE Syntax in Xref ({sum(len(values) for values in self.malformed_curies.values())})

{self._malformed_curies_table()}
"""

    def _unknown_prefix_md(self):
        return f"""
## Unknown Prefixes ({len(self.unknown_prefixes)})

{_tabulate_dd(self.unknown_prefixes, name="prefix")}
"""

    def _noncanonical_prefix_md(self):
        return f"""
## Non-canonical Prefixes ({len(self.noncanonical_prefixes)})

{_tabulate_dd(self.noncanonical_prefixes, name="prefix")}
        """

    def _invalid_identifiers_table(self):
        bvi = [
            (node_id, xref)
            for node_id, xrefs in sorted(self.invalid_luids.items())
            for xref in sorted(xrefs)
        ]
        return tabulate(bvi, headers=["node_id", "xref"], tablefmt="github")

    def _invalid_identifiers_md(self):
        return f"""
## Invalid Identifiers

{self._invalid_identifiers_table()}
        """

    def as_str(self) -> str:
        x = [
            f"## Versions: {self.versions}",
        ]
        if self.malformed_curies:
            x.append(self._bad_values_md())
        if self.unknown_prefixes:
            x.append(self._unknown_prefix_md())
        if self.noncanonical_prefixes:
            x.append(self._noncanonical_prefix_md())
        if self.invalid_luids:
            x.append(self._invalid_identifiers_md())
        return "\n".join(x)


PROTOCOLS = {"http://", "https://"}
SKIP_PREFIXES = {
    # Decomissioned
    "gaz",
    # Too big during development
    "chebi",
    "ncbitaxon",
    "pr",
    # Problem parsing both OWL and JSON
    "gsso",
    # Overwhelming amount of trash
    "txpo",
}


def check_prefix(prefix: str, cache: bool = False, *, iri_filter: Optional[str] = None) -> Results:
    if prefix != bioregistry.normalize_prefix(prefix):
        raise ValueError("this function requires bioregistry canonical prefixes")

    json_iri = bioregistry.get_json_download(prefix)
    if json_iri is not None:
        if cache:
            data = pystow.ensure_json("bio", "obofoundry", url=json_iri)
            return check_graph(data, iri_filter=iri_filter)
        try:
            data = requests.get(json_iri).json()
        except json.decoder.JSONDecodeError:
            click.secho(
                f"{prefix} json could not be parsed at {json_iri}. Falling back to OWL", fg="red"
            )
        else:
            return check_graph(data, iri_filter=iri_filter)

    owl_iri = bioregistry.get_owl_download(prefix)
    if owl_iri is not None:
        if cache:
            module = pystow.module("bio", "obofoundry", prefix)
            owl_path: Path = module.ensure(url=owl_iri)
            json_path: Path = module.join(name=owl_path.name).with_suffix(".json")
            data, messages = robot_parse_json_local(owl_path, json_path)
        else:
            data, messages = robot_parse_json_remote(owl_iri)
        if messages:
            click.secho(f"Output from parsing {prefix}", fg="blue")
            click.secho(messages, fg="blue")
        return check_graph(data, iri_filter=iri_filter)

    raise ValueError(f"no OWL IRI available for Bioregistry prefix {prefix}")


def check_iri(iri: str, *, iri_filter: Optional[str] = None) -> Results:
    data, messages = robot_parse_json_remote(iri)
    if messages:
        click.secho(f"Output from parsing {iri}", fg="blue")
        click.secho(messages, fg="blue")
    return check_graph(data, iri_filter=iri_filter)


def check_graph(data: Graphs, *, iri_filter: Optional[str] = None) -> Results:
    unknown_prefixes = defaultdict(dict)
    noncanonical_prefixes = defaultdict(dict)
    malformed_curies = defaultdict(set)
    invalid_luids = defaultdict(set)
    versions: dict[str, Optional[str]] = {}
    for graph_index, graph in enumerate(data["graphs"]):
        # this is the URI for the ontology, e.g. "http://purl.obolibrary.org/obo/go.owl"
        graph_id = graph["id"]

        # This contains metadata for the graph
        graph_meta = graph.get("meta", {})
        version = graph_meta.get("version")

        versions[graph_id] = version
        for node in graph["nodes"]:
            node_id = node["id"]
            if iri_filter and not node_id.startswith(iri_filter):
                continue
            node_meta = node.get("meta")
            if node_meta is None:
                continue

            definition = node_meta.get("definition", {})
            definition_xrefs = definition.get("xrefs", [])

            node_xrefs = node_meta.get("xrefs", [])
            for xref in node_xrefs:
                xref_curie = xref["val"]

                # Check that the CURIE syntax is used properly
                try:
                    xref_prefix, xref_identifier = xref_curie.split(":", 1)
                except ValueError:
                    malformed_curies[node_id].add(xref_curie)
                    continue

                # Disregard URIs
                if xref_prefix in {"http", "https", "urn"}:
                    continue  # check some other time

                # Check that the canonical Bioregistry prefix is used
                norm_xref_prefix = bioregistry.normalize_prefix(xref_prefix)
                if norm_xref_prefix is None:
                    unknown_prefixes[xref_prefix][node_id] = xref_curie
                elif norm_xref_prefix.casefold() != xref_prefix.casefold():
                    noncanonical_prefixes[xref_prefix][node_id] = xref_curie

                # Check that the identifier validates against the prefix's regex
                pattern = bioregistry.get_pattern(xref_prefix)
                if pattern and not re.match(pattern, xref_identifier):
                    invalid_luids[node_id].add(xref_curie)

            # for prop in node_meta.get("basicPropertyValues", []):
            #     pass
        # for edge in graph["edges"]:
        #     pass

    return Results(
        versions=versions,
        unknown_prefixes=unknown_prefixes,
        malformed_curies=malformed_curies,
        noncanonical_prefixes=noncanonical_prefixes,
        invalid_luids=invalid_luids,
    )


def _get_version(graph: Graph) -> Optional[str]:
    return None


def _tabulate_dd(dd, name) -> str:
    rows = []
    for key, values in dd.items():
        rows.append((key, len(values), *random.choice(list(values.items()))))
    rows = sorted(rows, key=itemgetter(1), reverse=True)
    return tabulate(
        rows, headers=[name, "count", "example_node_id", "example_xref"], tablefmt="github"
    )


@click.command()
@click.argument("inp")
@click.option("--cache", is_flag=True)
@click.option("--iri-filter")
@verbose_option
def main(inp: str, cache: bool, iri_filter: Optional[str]):
    """Analyze a given ontology."""
    if any(inp.startswith(protocol) for protocol in PROTOCOLS):
        results = check_iri(inp, iri_filter=iri_filter)
    elif (prefix := bioregistry.normalize_prefix(inp)) is not None:
        results = check_prefix(prefix, cache=cache, iri_filter=iri_filter)
    else:
        click.secho(f"Input is neither an IRI nor valid prefix in the Bioregistry: {inp}", fg="red")
        sys.exit(-1)

    result_str = results.as_str()
    try:
        path = pystow.join("oquat", name=f"{prefix}.md")
    except NameError:
        click.echo(result_str)
    else:
        path.write_text(result_str)
        click.echo(f"Results for {prefix} written to {path}")


if __name__ == "__main__":
    main()
