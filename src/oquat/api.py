# -*- coding: utf-8 -*-

"""Ontology analysis."""

import dataclasses
import datetime
import logging
import random
import re
import sys
from collections import defaultdict
from functools import lru_cache
from operator import itemgetter
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Optional, Set, Union

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

DOWNLOAD_BEFORE_PARSING = {"caloha", "genepio"}


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
    unknown_prefixes: Dict[str, Dict[str, str]]
    noncanonical_prefixes: Dict[str, Dict[str, str]]
    malformed_curies: Dict[str, List[str]]
    invalid_luids: Dict[str, List[str]]

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
    """A package of assessment on a single graph."""

    graph_id: str
    version_iri: Optional[str]
    version: Optional[str]
    xref_pack: ResultPack
    prov_pack: ResultPack
    synonym_pack: ResultPack
    # edge_pack: ResultPack

    def to_markdown(self):
        """Build a markdown string."""
        return f"""\
## Ontology Metadata

Graph Identifier: {self.graph_id}

Graph Version: {self.version}/{self.version_iri}

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
    # Problem parsing both OWL and JSON
    "gsso",
    # Overwhelming amount of trash
    "txpo",
    "epio",
}
NONCANONICAL_EXCEPTIONS = {
    "Wikipedia",
    "PMID",
}


class NoParsableURIs(ValueError):
    """Raised when none of the URIs work."""


class AnalysisResults(pydantic.BaseModel):
    """Results from analysis and messages from the journey."""

    results: Dict[str, Results] = pydantic.Field(default_factory=dict)
    messages: List[str] = pydantic.Field(default_factory=list)
    created: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)


def analyze_by_prefix(
    prefix: str, *, cache: bool = False, iri_filter: Optional[str] = None
) -> AnalysisResults:
    """Analyze an ontology based on a given Bioregistry prefix."""
    parse_results = get_obograph_by_prefix(prefix, cache=cache or prefix in DOWNLOAD_BEFORE_PARSING)
    if parse_results.graph_document is None:
        return AnalysisResults(
            results={},
            messages=parse_results.messages,
        )
    return AnalysisResults(
        results=analyze_graphs(
            parse_results.graph_document, iri_filter=iri_filter, iri=parse_results.iri
        ),
        messages=parse_results.messages,
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
        messages=parse_results.messages,
    )


def analyze_by_iri(iri: str, *, iri_filter: Optional[str] = None) -> AnalysisResults:
    """Analyze an ontology at a given IRI."""
    parse_results = convert_to_obograph_remote(iri)
    if parse_results.messages:
        secho(f"Output from parsing {iri}", fg="blue")
        secho("\n".join(parse_results.messages), fg="blue")
    return AnalysisResults(
        results=analyze_graphs(parse_results.graphs, iri_filter=iri_filter, iri=iri),
        messages=parse_results.messages,
    )


class MissingGraphIRI(KeyError):
    """Raised for graphs with no IRI."""


def analyze_graphs(
    graph_document: GraphDocument,
    *,
    iri_filter: Optional[str] = None,
    iri: Optional[str] = None,
) -> Dict[str, Results]:
    """Analyze an ontology that's pre-parsed into an OBO graph."""
    results = [analyze_graph(graph, iri_filter=iri_filter) for graph in graph_document.graphs]
    if len(results) == 1 and not results[0].graph_id:
        if iri is None:
            raise MissingGraphIRI
        # if there's only one graph and it's missing an ID, then let it pass
        logger.warning("missing graph IRI, using %s", iri)
        return {iri: results[0]}
    elif not all(r.graph_id for r in results):
        raise MissingGraphIRI
    else:
        return {r.graph_id: r for r in results}


def analyze_graph(graph: Graph, *, iri_filter: Optional[str] = None) -> Results:
    """Analyze a single graph."""
    node_xref_pack = PrePack("Node Xrefs")
    prov_xref_pack = PrePack("Provenance Xrefs")
    syn_xref_pack = PrePack("Synonym Xrefs")
    # edge_pack = PrePack("Edges")

    # if graph.id is None:
    #     # this is the URI for the ontology, e.g. "http://purl.obolibrary.org/obo/go.owl"
    #     raise MissingGraphIRI

    for node in tqdm(graph.nodes, unit_scale=True, unit="node", leave=False):
        node_id = node.id
        if iri_filter and not node_id.startswith(iri_filter):
            continue
        node_meta = node.meta
        if node_meta is None:
            continue

        node_xrefs = node_meta.xrefs
        for node_xref_dict in node_xrefs or []:
            node_xref_pack.aggregate_curie_issues(node_id, node_xref_dict.value_raw)

        definition_xrefs = node_meta.definition and node_meta.definition.xrefs_raw
        for prov_xref_curie in definition_xrefs or []:
            prov_xref_pack.aggregate_curie_issues(
                node_id=node_id,
                curie=prov_xref_curie,
            )

        for synonym in node_meta.synonyms or []:
            for synonym_xref_curie in synonym.xrefs_raw or []:
                syn_xref_pack.aggregate_curie_issues(
                    node_id=node_id,
                    curie=synonym_xref_curie,
                    # A lot of times they stick random stuff
                    # in here that aren't CURIEs
                    track_non_curies=False,
                )

        # for prop in node_meta.get("basicPropertyValues", []):
        #     pass

    # for edge in tqdm(graph.edges, unit_scale=True, unit="edge", leave=False):
    #     if iri_filter and not edge.sub.startswith(iri_filter):
    #         continue
    #     if edge.pred != "is_a":
    #         secho(str(edge))
    #     edge_pack.aggregate_curie_issues(edge.sub, edge.sub)
    #     edge_pack.aggregate_curie_issues(edge.sub, edge.pred)
    #     edge_pack.aggregate_curie_issues(edge.sub, edge.obj)

    return Results(
        graph_id=graph.id,
        version=graph.version,
        version_iri=graph.version_iri,
        xref_pack=node_xref_pack.finalize(),
        prov_pack=prov_xref_pack.finalize(),
        synonym_pack=syn_xref_pack.finalize(),
        # edge_pack=edge_pack.finalize(),
    )


class PrePack:
    """A pre-results pack for aggregating then finalizing."""

    def __init__(self, label: str):
        """Initialize the pre-results pack."""
        self.label = label
        self.unknown_prefixes: DefaultDict[str, Dict[str, str]] = defaultdict(dict)
        self.noncanonical_prefixes: DefaultDict[str, Dict[str, str]] = defaultdict(dict)
        self.malformed_curies: DefaultDict[str, Set[str]] = defaultdict(set)
        self.invalid_luids: DefaultDict[str, Set[str]] = defaultdict(set)

    def aggregate_curie_issues(
        self,
        node_id: str,
        curie: str,
        track_non_curies: bool = True,
    ):
        """Add an issue with a CURIE."""
        _aggregate_curie_issues(
            node_id,
            curie,
            self.malformed_curies,
            self.unknown_prefixes,
            self.noncanonical_prefixes,
            self.invalid_luids,
            track_non_curies=track_non_curies,
        )

    def finalize(self):
        """Finalize the results pack."""
        return ResultPack(
            label=self.label,
            unknown_prefixes=dict(self.unknown_prefixes),
            malformed_curies=_canonicalize_dict(self.malformed_curies),
            noncanonical_prefixes=dict(self.noncanonical_prefixes),
            invalid_luids=_canonicalize_dict(self.invalid_luids),
        )


def _canonicalize_dict(dd: DefaultDict[str, Set[str]]) -> Dict[str, List[str]]:
    return {k: sorted(v) for k, v in dd.items()}


SKIP_ISSUES = {"type", "is_a", "subPropertyOf"}


@lru_cache(maxsize=None)
def _get_pattern(prefix: str):
    p = bioregistry.get_pattern(prefix)
    if not p:
        return None
    return re.compile(p)


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
    if curie in SKIP_ISSUES:
        return
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
    pattern = _get_pattern(prefix)
    if pattern and pattern.fullmatch(identifier) is None:
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
        if norm_prefix is None:
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
