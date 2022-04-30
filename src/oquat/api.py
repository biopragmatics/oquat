# -*- coding: utf-8 -*-

"""Ontology analysis."""

import dataclasses
import logging
import random
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from operator import itemgetter
from pathlib import Path
from typing import Any, DefaultDict, Optional, Union

import bioregistry
import click
import pydantic
import pystow
from bioontologies import get_obograph_by_prefix
from bioontologies.obograph import Graph, GraphDocument
from bioontologies.robot import convert_to_obograph_local, convert_to_obograph_remote
from more_click import verbose_option
from pydantic import BaseModel
from pydantic.json import ENCODERS_BY_TYPE
from tabulate import tabulate
from tqdm import tqdm

logger = logging.getLogger(__name__)


def secho(s: str, fg=None) -> None:
    """Write text in tqdm with :func:`click.style`."""
    tqdm.write(click.style(s, fg=fg))


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
    malformed_curies: dict[str, list[str]]
    invalid_luids: dict[str, list[str]]

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
    "ncbitaxon",
    "pr",
    # Problem parsing both OWL and JSON
    "gsso",
    # Overwhelming amount of trash
    "txpo",
}
NONCANONICAL_EXCEPTIONS = {
    "Wikipedia",
    "PMID",
}


class NoParsableURIs(ValueError):
    """Raised when none of the URIs work."""


@dataclass
class AnalysisResults:
    """Results from analysis and messages from the journey."""

    results: dict[str, Results]
    messages: list[str]


def analyze_by_prefix(
    prefix: str, *, cache: bool = False, iri_filter: Optional[str] = None
) -> AnalysisResults:
    """Analyze an ontology based on a given Bioregistry prefix."""
    parse_results = get_obograph_by_prefix(prefix)
    return AnalysisResults(
        results=analyze_graphs(parse_results.graph_document, iri_filter=iri_filter),
        messages=[],
    )


def analyze_by_path(path: Union[str, Path], *, iri_filter: Optional[str] = None) -> AnalysisResults:
    """Analyze an ontology at a given IRI."""
    path = Path(path).resolve()
    parse_results = convert_to_obograph_local(path)
    if parse_results.messages:
        secho(f"Output from parsing {path}", fg="blue")
        secho("\n".join(parse_results.messages), fg="blue")
    return AnalysisResults(
        results=analyze_graphs(parse_results.graphs, iri_filter=iri_filter),
        messages=[],
    )


def analyze_by_iri(iri: str, *, iri_filter: Optional[str] = None) -> AnalysisResults:
    """Analyze an ontology at a given IRI."""
    parse_results = convert_to_obograph_remote(iri)
    if parse_results.messages:
        secho(f"Output from parsing {iri}", fg="blue")
        secho("\n".join(parse_results.messages), fg="blue")
    return AnalysisResults(
        results=analyze_graphs(parse_results.graphs, iri_filter=iri_filter),
        messages=[],
    )


class MissingGraphIRI(KeyError):
    """Raised for graphs with no IRI."""


def analyze_graphs(
    graph_document: GraphDocument, *, iri_filter: Optional[str] = None
) -> dict[str, Results]:
    """Analyze an ontology that's pre-parsed into an OBO graph."""
    it = (analyze_graph(graph, iri_filter=iri_filter) for graph in graph_document.graphs)
    return {results.graph_id: results for results in it}


def analyze_graph(graph: Graph, *, iri_filter: Optional[str] = None) -> Results:
    """Analyze a single graph."""
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
    graph_id = graph.id
    if graph_id is None:
        raise MissingGraphIRI

    # This contains metadata for the graph
    graph_meta = graph.meta
    version = graph.version_iri

    for node in graph.nodes:
        node_id = node.id
        if iri_filter and not node_id.startswith(iri_filter):
            continue
        node_meta = node.meta
        if node_meta is None:
            continue

        node_xrefs = node_meta.xrefs
        for node_xref_dict in node_xrefs or []:
            _aggregate_curie_issues(
                node_id,
                node_xref_dict.val,
                node_xref_malformed_curies,
                node_xref_unknown_prefixes,
                node_xref_noncanonical_prefixes,
                node_xref_invalid_luids,
            )

        definition = node_meta.definition
        definition_xrefs = node_meta.definition and node_meta.definition.xrefs
        for prov_xref_curie in definition_xrefs or []:
            _aggregate_curie_issues(
                node_id,
                prov_xref_curie,
                prov_xref_malformed_curies,
                prov_xref_unknown_prefixes,
                prov_xref_noncanonical_prefixes,
                prov_xref_invalid_luids,
            )

        for synonym in node_meta.synonyms or []:
            for synoynm_xref_curie in synonym.xrefs or []:
                _aggregate_curie_issues(
                    node_id,
                    synoynm_xref_curie,
                    syn_xref_malformed_curies,
                    syn_xref_unknown_prefixes,
                    syn_xref_noncanonical_prefixes,
                    syn_xref_invalid_luids,
                    # A lot of times they stick random stuff
                    # in here that aren't CURIEs
                    track_non_curies=False,
                )

        # for prop in node_meta.get("basicPropertyValues", []):
        #     pass
    # for edge in graph["edges"]:
    #     pass

    return Results(
        graph_id=graph_id,
        version=version,
        xref_pack=ResultPack(
            label="Node Xrefs",
            unknown_prefixes=node_xref_unknown_prefixes,
            malformed_curies=_canonicalize_dict(node_xref_malformed_curies),
            noncanonical_prefixes=node_xref_noncanonical_prefixes,
            invalid_luids=_canonicalize_dict(node_xref_invalid_luids),
        ),
        prov_pack=ResultPack(
            label="Provenance Xrefs",
            unknown_prefixes=prov_xref_unknown_prefixes,
            malformed_curies=_canonicalize_dict(prov_xref_malformed_curies),
            noncanonical_prefixes=prov_xref_noncanonical_prefixes,
            invalid_luids=_canonicalize_dict(prov_xref_invalid_luids),
        ),
        synonym_pack=ResultPack(
            label="Synonym Xrefs",
            unknown_prefixes=syn_xref_unknown_prefixes,
            malformed_curies=_canonicalize_dict(syn_xref_malformed_curies),
            noncanonical_prefixes=syn_xref_noncanonical_prefixes,
            invalid_luids=_canonicalize_dict(syn_xref_invalid_luids),
        ),
    )


def _canonicalize_dict(dd: DefaultDict[str, set[str]]) -> dict[str, list[str]]:
    return {k: sorted(v) for k, v in dd.items()}


def _aggregate_curie_issues(
    node_id,
    curie,
    malformed_curies,
    unknown_prefixes,
    noncanonical_prefixes,
    invalid_luids,
    *,
    track_non_curies: bool = True,
) -> None:
    # Check that the CURIE syntax is used properly
    try:
        prefix, identifier = curie.split(":", 1)
    except ValueError:
        if track_non_curies:
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
        if prefix not in NONCANONICAL_EXCEPTIONS:
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


def coalesce_filters(prefix, iri_filter, obo_filter):
    """Coalesce IRI and OBO filter."""
    if not obo_filter:
        return iri_filter
    if iri_filter:
        logger.info(f"[{prefix}] IRI filter overrides OBO filter, using {iri_filter}")
        return iri_filter
    iri_filter = bioregistry.get_obofoundry_uri_prefix(prefix)
    if iri_filter:
        logger.info(f"[{prefix}] Filtering to nodes originating from {iri_filter}")
    else:
        logger.debug(f"[{prefix}] Could not generate an OBO URI prefix")
    return iri_filter


@click.command()
@click.option("--iri")
@click.option("--prefix")
@click.option("--path", type=Path)
@click.option("--cache", is_flag=True)
@click.option("--iri-filter")
@click.option("-o", "--obo-filter", is_flag=True)
@verbose_option
def analyze(
    iri: Optional[str],
    prefix: Optional[str],
    path: Optional[Path],
    cache: bool,
    iri_filter: Optional[str],
    obo_filter: bool,
):
    """Analyze a given ontology."""
    analysis_results: AnalysisResults

    if 1 != sum(arg is not None for arg in (iri, prefix, path)):
        secho("Can only pass one of --iri, --prefix, and --path")
        return sys.exit(-1)
    elif path is not None:
        path = path.resolve()
        if not path.is_file():
            secho(f"File does not exist: {path}")
            return sys.exit(-1)
        analysis_results = analyze_by_path(path, iri_filter=iri_filter)
    elif iri is not None:
        analysis_results = analyze_by_iri(iri, iri_filter=iri_filter)
    elif prefix is not None:
        norm_prefix = bioregistry.normalize_prefix(prefix)
        if norm_prefix is not None:
            secho(f"An invalid Bioregistry prefix was given: {prefix}")
            return sys.exit(-1)
        iri_filter = coalesce_filters(norm_prefix, iri_filter, obo_filter)
        analysis_results = analyze_by_prefix(prefix, cache=cache, iri_filter=iri_filter)
    else:
        # This can't happen
        return sys.exit(-1)

    result_str = "\n".join(v.to_markdown() for v in analysis_results.results.values())
    if prefix is not None:
        output_path = pystow.join("oquat", name=f"{prefix}.md")
        output_path.write_text(result_str)
        click.echo(f"Results for {prefix} written to {output_path}")
    else:
        click.echo(result_str)


if __name__ == "__main__":
    analyze()
