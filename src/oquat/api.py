# -*- coding: utf-8 -*-

"""Ontology analysis."""

import dataclasses
import json.decoder
import random
import re
import sys
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import Any, DefaultDict, Optional

import bioregistry
import click
import pydantic
import pystow
import requests
from more_click import verbose_option
from pydantic import BaseModel
from pydantic.json import ENCODERS_BY_TYPE
from tabulate import tabulate

from .robot import robot_parse_json_local, robot_parse_json_remote
from .struct.obograph import Graphs


def extended_encoder(obj: Any) -> Any:
    """Encode objects similarly to :func:`pydantic.json.pydantic_encoder`."""
    if isinstance(obj, BaseModel):
        return obj.dict(exclude_none=True)
    elif dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)

    # Check the class type and its superclasses for a matching encoder
    for base in obj.__class__.__mro__[:-1]:
        try:
            encoder = ENCODERS_BY_TYPE[base]
        except KeyError:
            continue
        return encoder(obj)
    else:  # We have exited the for loop without finding a suitable encoder
        raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")


class ResultPack(pydantic.BaseModel):
    """A set of results for CURIE analysis."""

    label: str
    unknown_prefixes: dict[str, dict[str, str]]
    noncanonical_prefixes: dict[str, dict[str, str]]
    malformed_curies: dict[str, set[str]]
    invalid_luids: dict[str, set[str]]

    def _malformed_curies_table(self):
        bvi = [
            (k, v) for k, values in sorted(self.malformed_curies.items()) for v in sorted(values)
        ]
        return tabulate(bvi, headers=["node_id", "xref"], tablefmt="github")

    def _bad_values_md(self):
        return f"""
### {self.label} Invalid CURIE Syntax in Xref ({sum(len(values) for values in self.malformed_curies.values())})

{self._malformed_curies_table()}
"""

    def _unknown_prefix_md(self):
        return f"""
### {self.label} Unknown Prefixes ({len(self.unknown_prefixes)})

{_tabulate_dd(self.unknown_prefixes, name="prefix")}
"""

    def _noncanonical_prefix_md(self):
        return f"""
### {self.label} Non-canonical Prefixes ({len(self.noncanonical_prefixes)})

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
### {self.label} Invalid Identifiers ({sum(len(v) for v in self.invalid_luids.values())})

{self._invalid_identifiers_table()}
        """

    def to_markdown(self) -> str:
        """Build a markdown string."""
        x = []
        if self.malformed_curies:
            x.append(self._bad_values_md())
        if self.unknown_prefixes:
            x.append(self._unknown_prefix_md())
        if self.noncanonical_prefixes:
            x.append(self._noncanonical_prefix_md())
        if self.invalid_luids:
            x.append(self._invalid_identifiers_md())
        return "\n".join(x)


class Results(pydantic.BaseModel):
    """A package of assessment results."""

    graph_id: str
    version: Optional[str]
    xref_pack: ResultPack
    prov_pack: ResultPack
    synonym_pack: ResultPack

    def to_markdown(self):
        """Build a markdown string."""
        return f"""\
## Ontology Metadata

Graph Identifier: {self.graph_id}

Graph Version: {self.version}

{self.xref_pack.to_markdown()}

{self.prov_pack.to_markdown()}

{self.synonym_pack.to_markdown()}
        """


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


def analyze_by_prefix(
    prefix: str, cache: bool = False, *, iri_filter: Optional[str] = None
) -> dict[str, Results]:
    """Analyze an ontology based on a given Bioregistry prefix."""
    if prefix != bioregistry.normalize_prefix(prefix):
        raise ValueError("this function requires bioregistry canonical prefixes")

    json_iri = bioregistry.get_json_download(prefix)
    if json_iri is not None:
        if cache:
            data = pystow.ensure_json("bio", "obofoundry", url=json_iri)
            return analyze_graph(data, iri_filter=iri_filter)
        try:
            data = requests.get(json_iri).json()
        except json.decoder.JSONDecodeError:
            click.secho(
                f"{prefix} json could not be parsed at {json_iri}. Falling back to OWL", fg="red"
            )
        else:
            return analyze_graph(data, iri_filter=iri_filter)

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
        return analyze_graph(data, iri_filter=iri_filter)

    raise ValueError(f"no OWL IRI available for Bioregistry prefix {prefix}")


def analyze_by_iri(iri: str, *, iri_filter: Optional[str] = None) -> dict[str, Results]:
    """Analyze an ontology at a given IRI."""
    data, messages = robot_parse_json_remote(iri)
    if messages:
        click.secho(f"Output from parsing {iri}", fg="blue")
        click.secho(messages, fg="blue")
    return analyze_graph(data, iri_filter=iri_filter)


def analyze_graph(data: Graphs, *, iri_filter: Optional[str] = None) -> dict[str, Results]:
    """Analyze an ontology that's pre-parsed into an OBO graph."""
    rv = {}
    for graph in data["graphs"]:
        node_xref_unknown_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        node_xref_noncanonical_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        node_xref_malformed_curies: DefaultDict[str, set[str]] = defaultdict(set)
        node_xref_invalid_luids: DefaultDict[str, set[str]] = defaultdict(set)

        prov_xref_unknown_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        prov_xref_noncanonical_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        prov_xref_malformed_curies: DefaultDict[str, set[str]] = defaultdict(set)
        prov_xref_invalid_luids: DefaultDict[str, set[str]] = defaultdict(set)

        syn_xref_unknown_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        syn_xref_noncanonical_prefixes: DefaultDict[str, dict[str, str]] = defaultdict(dict)
        syn_xref_malformed_curies: DefaultDict[str, set[str]] = defaultdict(set)
        syn_xref_invalid_luids: DefaultDict[str, set[str]] = defaultdict(set)

        # this is the URI for the ontology, e.g. "http://purl.obolibrary.org/obo/go.owl"
        graph_id = graph["id"]

        # This contains metadata for the graph
        graph_meta = graph.get("meta", {})
        version = graph_meta.get("version")

        for node in graph["nodes"]:
            node_id = node["id"]
            if iri_filter and not node_id.startswith(iri_filter):
                continue
            node_meta = node.get("meta")
            if node_meta is None:
                continue

            node_xrefs = node_meta.get("xrefs", [])
            for node_xref_dict in node_xrefs:
                _aggregate_curie_issues(
                    node_id,
                    node_xref_dict["val"],
                    node_xref_malformed_curies,
                    node_xref_unknown_prefixes,
                    node_xref_noncanonical_prefixes,
                    node_xref_invalid_luids,
                )

            definition_xrefs = node_meta.get("definition", {}).get("xrefs", [])
            for prov_xref_curie in definition_xrefs:
                _aggregate_curie_issues(
                    node_id,
                    prov_xref_curie,
                    prov_xref_malformed_curies,
                    prov_xref_unknown_prefixes,
                    prov_xref_noncanonical_prefixes,
                    prov_xref_invalid_luids,
                )

            synonyms = node_meta.get("synonyms", [])
            for synonym in synonyms:
                for synoynm_xref_curie in synonym.get("xrefs", []):
                    _aggregate_curie_issues(
                        node_id,
                        synoynm_xref_curie,
                        syn_xref_malformed_curies,
                        syn_xref_unknown_prefixes,
                        syn_xref_noncanonical_prefixes,
                        syn_xref_invalid_luids,
                    )

            # for prop in node_meta.get("basicPropertyValues", []):
            #     pass
        # for edge in graph["edges"]:
        #     pass

        rv[graph_id] = Results(
            graph_id=graph_id,
            version=version,
            xref_pack=ResultPack(
                label="Node Xrefs",
                unknown_prefixes=node_xref_unknown_prefixes,
                malformed_curies=node_xref_malformed_curies,
                noncanonical_prefixes=node_xref_noncanonical_prefixes,
                invalid_luids=node_xref_invalid_luids,
            ),
            prov_pack=ResultPack(
                label="Provenance Xrefs",
                unknown_prefixes=prov_xref_unknown_prefixes,
                malformed_curies=prov_xref_malformed_curies,
                noncanonical_prefixes=prov_xref_noncanonical_prefixes,
                invalid_luids=prov_xref_invalid_luids,
            ),
            synonym_pack=ResultPack(
                label="Synonym Xrefs",
                unknown_prefixes=syn_xref_unknown_prefixes,
                malformed_curies=syn_xref_malformed_curies,
                noncanonical_prefixes=syn_xref_noncanonical_prefixes,
                invalid_luids=syn_xref_invalid_luids,
            ),
        )

    return rv


def _aggregate_curie_issues(
    node_id,
    curie,
    malformed_curies,
    unknown_prefixes,
    noncanonical_prefixes,
    invalid_luids,
) -> None:
    # Check that the CURIE syntax is used properly
    try:
        prefix, identifier = curie.split(":", 1)
    except ValueError:
        malformed_curies[node_id].add(curie)
        return

    # Disregard URIs
    if prefix in {"http", "https", "urn"}:
        return  # check some other time

    # Check that the canonical Bioregistry prefix is used
    norm_prefix = bioregistry.normalize_prefix(prefix)
    if norm_prefix is None:
        unknown_prefixes[prefix][node_id] = curie
    elif norm_prefix.casefold() != prefix.casefold():
        noncanonical_prefixes[prefix][node_id] = curie

    # Check that the identifier validates against the prefix's regex
    pattern = bioregistry.get_pattern(prefix)
    if pattern and not re.match(pattern, identifier):
        invalid_luids[node_id].add(curie)


def _tabulate_dd(dd, name) -> str:
    rows = []
    for key, values in dd.items():
        rows.append((key, len(values), *random.choice(list(values.items()))))  # noqa:S311
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
        results = analyze_by_iri(inp, iri_filter=iri_filter)
    elif (prefix := bioregistry.normalize_prefix(inp)) is not None:
        results = analyze_by_prefix(prefix, cache=cache, iri_filter=iri_filter)
    else:
        click.secho(f"Input is neither an IRI nor valid prefix in the Bioregistry: {inp}", fg="red")
        sys.exit(-1)

    result_str = "\n".join(v.to_markdown() for v in results.values())
    try:
        path = pystow.join("oquat", name=f"{prefix}.md")
    except NameError:
        click.echo(result_str)
    else:
        path.write_text(result_str)
        click.echo(f"Results for {prefix} written to {path}")


if __name__ == "__main__":
    main()
