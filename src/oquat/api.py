"""Ontology analysis."""

from __future__ import annotations

import datetime
import logging
import random
import re
import sys
import tempfile
from collections import defaultdict
from functools import cache
from pathlib import Path

import bioregistry
import click
import obographs
import pydantic
import pystow
from more_click import verbose_option
from obographs import GraphDocument
from tabulate import tabulate
from tqdm import tqdm

logger = logging.getLogger(__name__)

DOWNLOAD_BEFORE_PARSING = {"caloha", "genepio"}
CACHE_MODULE = pystow.module("oquat", "data")


def secho(s: str, fg=None) -> None:
    """Write text in tqdm with :func:`click.style`."""
    tqdm.write(click.style(s, fg=fg))


class ResultPack(pydantic.BaseModel):
    """A set of results for CURIE analysis."""

    label: str
    known_prefixes: dict[str, dict[str, str]] | None = None
    unknown_prefixes: dict[str, dict[str, str]]
    noncanonical_prefixes: dict[str, dict[str, str]]
    malformed_curies: dict[str, list[str]]
    invalid_luids: dict[str, list[str]]

    def _malformed_curies_table(self) -> tuple[int, str]:
        rows = [
            (k, v) for k, values in sorted(self.malformed_curies.items()) for v in sorted(values)
        ]
        return len(rows), tabulate(rows, headers=["node_id", "xref"], tablefmt="github")

    def _bad_values_md(self) -> str:
        n, table = self._malformed_curies_table()
        table = _wrap_table(table, n)
        n = sum(len(values) for values in self.malformed_curies.values())
        header = f"### {self.label} Invalid CURIE Syntax in Xref ({n:,})"
        return header + "\n\n" + table + "\n\n"

    def _unknown_prefix_md(self) -> str:
        n, table = _tabulate_dd(self.unknown_prefixes, name="prefix")
        table = _wrap_table(table, n)
        header = f"### {self.label} Unknown Prefixes ({len(self.unknown_prefixes):,})"
        return header + "\n\n" + table + "\n\n"

    def _noncanonical_prefix_md(self) -> str:
        n, table = _tabulate_dd(self.noncanonical_prefixes, name="prefix")
        table = _wrap_table(table, n)
        header = f"### {self.label} Non-canonical Prefixes ({len(self.noncanonical_prefixes):,})"
        return header + "\n\n" + table + "\n\n"

    def _invalid_identifiers_table(self) -> tuple[int, str]:
        xx = defaultdict(list)
        for node_id, xrefs in self.invalid_luids.items():
            for xref in xrefs:
                xx[xref].append(node_id)
        rows = []
        for key, values in xx.items():
            rows.append((key, len(values), random.choice(values)))
        rows = sorted(rows, key=lambda row: (row[1], row[0].casefold()), reverse=True)
        return len(rows), tabulate(
            rows, headers=["xref", "count", "example_node_id"], tablefmt="github"
        )

    def _invalid_identifiers_md(self) -> str:
        n, table = self._invalid_identifiers_table()
        table = _wrap_table(table, n)
        n = sum(len(v) for v in self.invalid_luids.values())
        header = f"### {self.label} Invalid Identifiers ({n:,})"
        return header + "\n\n" + table + "\n\n"

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
    version: str | None = None
    version_iri: str | None = None
    xref_pack: ResultPack | None = None
    prov_pack: ResultPack | None = None
    synonym_pack: ResultPack | None = None

    # edge_pack: ResultPack

    def to_markdown(self) -> str:
        """Build a markdown string."""
        rows: list[str] = [
            "## Ontology Metadata",
        ]
        if self.graph_id:
            rows.append(f"Graph Identifier: {self.graph_id}")
        if self.version or self.version_iri:
            rows.append(f"Graph Version: {self.version}/{self.version_iri}")
        if self.xref_pack:
            rows.append(self.xref_pack.to_markdown())
        if self.prov_pack:
            rows.append(self.prov_pack.to_markdown())
        if self.synonym_pack:
            rows.append(self.synonym_pack.to_markdown())
        return "\n\n".join(rows).strip()


def _wrap_table(table: str, n: int, max_n: int = 100) -> str:
    if n > max_n:
        return f"<details><summary>Details</summary>\n\n{table}\n\n</details>"
    return table


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


class NoParsableURIsError(ValueError):
    """Raised when none of the URIs work."""


class AnalysisResults(pydantic.BaseModel):
    """Results from analysis and messages from the journey."""

    results: dict[str, Results] = pydantic.Field(default_factory=dict)
    messages: list[str] = pydantic.Field(default_factory=list)
    created: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)


def analyze_by_prefix(
    prefix: str, *, cache: bool = False, iri_filter: str | None = None
) -> AnalysisResults:
    """Analyze an ontology based on a given Bioregistry prefix."""
    url = bioregistry.get_json_download(prefix)
    if url:
        if cache:
            try:
                path = CACHE_MODULE.ensure(url=url)
            except pystow.utils.DownloadError:
                tqdm.write(f"[{prefix} (json)] failed to download {url}")
            else:
                return analyze_by_path(path, iri_filter=iri_filter)
        else:
            return analyze_by_iri(url, iri_filter=iri_filter)

    from bioontologies.robot import convert

    for part, url in [
        ("owl", bioregistry.get_owl_download(prefix)),
        ("obo", bioregistry.get_obo_download(prefix)),
        ("ttl", bioregistry.get_rdf_download(prefix)),
    ]:
        if url is None:
            continue
        json_path = CACHE_MODULE.join(name=f"{prefix}.json")
        if not cache:
            # the convert command can take in a URL directly.
            path = url
        elif json_path.is_file():
            return analyze_by_path(json_path, iri_filter=iri_filter)
        else:
            try:
                path = CACHE_MODULE.ensure(url=url)
            except pystow.utils.DownloadError:
                tqdm.write(f"[{prefix} ({part})] failed to download {url}")
                continue
        try:
            convert(path, json_path)
        except Exception:
            tqdm.write(f"[{prefix} ({part})] failed to convert")
        else:
            return analyze_by_path(json_path, iri_filter=iri_filter)

    return AnalysisResults()


def analyze_by_path(path: str | Path, *, iri_filter: str | None = None) -> AnalysisResults:
    """Analyze an ontology at a given IRI."""
    graph_document = _read(Path(path).expanduser().resolve())
    return AnalysisResults(
        results=analyze_graphs(graph_document, iri_filter=iri_filter),
    )


def analyze_by_iri(iri: str, *, iri_filter: str | None = None) -> AnalysisResults:
    """Analyze an ontology at a given IRI."""
    graph_document = _read(iri)
    return AnalysisResults(
        results=analyze_graphs(graph_document, iri_filter=iri_filter, iri=iri),
    )


def _read(s: str | Path) -> GraphDocument:
    if str(s).endswith(".json"):
        return obographs.read(s, squeeze=False)
    elif any(str(s).endswith(x) for x in (".obo", ".owl", ".ttl")):
        from bioontologies.robot import convert

        with tempfile.TemporaryDirectory() as d:
            json_path = Path(d).joinpath("temp.json")
            try:
                convert(s, json_path)
            except Exception:
                tqdm.write(f"failed to convert {s}")
                raise
            else:
                rv = obographs.read(json_path, squeeze=False)
        return rv
    else:
        raise ValueError(f"Invalid file extension: {s}")


class MissingGraphIRIError(KeyError):
    """Raised for graphs with no IRI."""


def analyze_graphs(
    graph_document: obographs.GraphDocument,
    *,
    iri_filter: str | None = None,
    iri: str | None = None,
) -> dict[str, Results]:
    """Analyze an ontology that's pre-parsed into an OBO graph."""
    results = [analyze_graph(graph, iri_filter=iri_filter) for graph in graph_document.graphs]
    if len(results) == 1 and not results[0].graph_id:
        if iri is None:
            raise MissingGraphIRIError
        # if there's only one graph and it's missing an ID, then let it pass
        logger.warning("missing graph IRI, using %s", iri)
        return {iri: results[0]}
    elif not all(r.graph_id for r in results):
        raise MissingGraphIRIError
    else:
        return {r.graph_id: r for r in results}


def analyze_graph(graph: obographs.Graph, *, iri_filter: str | None = None) -> Results:
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

        for node_xref in node_meta.xrefs or []:
            node_xref_pack.aggregate_curie_issues(node_id, node_xref.val)

        definition_xrefs = node_meta.definition and node_meta.definition.xrefs
        for prov_xref_curie in definition_xrefs or []:
            prov_xref_pack.aggregate_curie_issues(
                node_id=node_id,
                curie=prov_xref_curie,
            )

        for synonym in node_meta.synonyms or []:
            for synonym_xref_curie in synonym.xrefs or []:
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
        version_iri=graph.meta.version if graph.meta else None,
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
        self.known_prefixes: defaultdict[str, dict[str, str]] = defaultdict(dict)
        self.unknown_prefixes: defaultdict[str, dict[str, str]] = defaultdict(dict)
        self.noncanonical_prefixes: defaultdict[str, dict[str, str]] = defaultdict(dict)
        self.malformed_curies: defaultdict[str, set[str]] = defaultdict(set)
        self.invalid_luids: defaultdict[str, set[str]] = defaultdict(set)

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
            self.known_prefixes,
            self.unknown_prefixes,
            self.noncanonical_prefixes,
            self.invalid_luids,
            track_non_curies=track_non_curies,
        )

    def finalize(self):
        """Finalize the results pack."""
        return ResultPack(
            label=self.label,
            known_prefixes=self.known_prefixes,
            unknown_prefixes=dict(self.unknown_prefixes),
            malformed_curies=_canonicalize_dict(self.malformed_curies),
            noncanonical_prefixes=dict(self.noncanonical_prefixes),
            invalid_luids=_canonicalize_dict(self.invalid_luids),
        )


def _canonicalize_dict(dd: defaultdict[str, set[str]]) -> dict[str, list[str]]:
    return {k: sorted(v) for k, v in dd.items()}


SKIP_ISSUES = {"type", "is_a", "subPropertyOf"}


@cache
def _get_pattern(prefix: str):
    p = bioregistry.get_pattern(prefix)
    if not p:
        return None
    return re.compile(p)


def _aggregate_curie_issues(
    node_id,
    curie,
    malformed_curies,
    known_prefixes,
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


def _tabulate_dd(dd, name) -> tuple[int, str]:
    rows = []
    for key, values in dd.items():
        rows.append((key, len(values), *random.choice(list(values.items()))))
    rows = sorted(rows, key=lambda row: (row[1], row[0].casefold()), reverse=True)
    return len(rows), tabulate(
        rows,
        headers=[name, "count", "example_node_id", "example_xref"],
        tablefmt="github",
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
@click.option("--iri", help="The IRI for an OBO Graph JSON, OBO, or OWL file")
@click.option(
    "--prefix",
    help="The prefix for the ontology. If given without an --iri or --path, "
    "will use the Bioregistry to find an appropriate IRI",
)
@click.option("--path", type=Path, help="The path to a local OBO Graph JSON, OBO, or OWL file")
@click.option("--cache", is_flag=True, help="Should a cache be used?")
@click.option(
    "--iri-filter",
    help="The URI prefix for terms in the ontology, e.g., "
    "`http://purl.obolibrary.org/obo/MONDO_` for the `mondo` ontology",
)
@click.option("-o", "--obo-filter", is_flag=True)
@verbose_option
def analyze(
    iri: str | None,
    prefix: str | None,
    path: Path | None,
    cache: bool,
    iri_filter: str | None,
    obo_filter: bool,
) -> None:
    """Analyze a given ontology."""
    analysis_results: AnalysisResults

    if iri and path:
        secho("Can only pass one of --iri or  --path")
        raise sys.exit(-1)
    elif path is not None:
        path = path.resolve()
        if not path.is_file():
            secho(f"File does not exist: {path}")
            raise sys.exit(-1)
        analysis_results = analyze_by_path(path, iri_filter=iri_filter)
    elif iri is not None:
        analysis_results = analyze_by_iri(iri, iri_filter=iri_filter)
    elif prefix is not None:
        norm_prefix = bioregistry.normalize_prefix(prefix)
        if norm_prefix is None:
            secho(f"An invalid Bioregistry prefix was given: {prefix}")
            raise sys.exit(-1)
        iri_filter = coalesce_filters(norm_prefix, iri_filter, obo_filter)
        analysis_results = analyze_by_prefix(prefix, cache=cache, iri_filter=iri_filter)
    else:
        # This can't happen
        raise sys.exit(-1)

    result_str = "\n".join(v.to_markdown() for v in analysis_results.results.values()).strip()
    if prefix is not None:
        output_path = pystow.join("oquat", name=f"{prefix}.md")
        output_path.write_text(result_str)
        click.echo(f"Results for {prefix} written to {output_path}")
    else:
        click.echo(result_str)


if __name__ == "__main__":
    analyze()
