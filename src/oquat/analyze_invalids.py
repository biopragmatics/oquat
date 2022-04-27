"""Analyze invalid identifiers."""

import json
import random
from collections import defaultdict
from operator import itemgetter
from textwrap import dedent

import bioregistry
from tabulate import tabulate
from tqdm import tqdm

from oquat.large_scale_analysis import DOCS, RESULTS

INVALIDS = DOCS.joinpath("invalids")
INVALIDS.mkdir(exist_ok=True, parents=True)
SOURCES = INVALIDS.joinpath("source")
SOURCES.mkdir(exist_ok=True, parents=True)
PREFIXES = INVALIDS.joinpath("prefix")
PREFIXES.mkdir(exist_ok=True, parents=True)
INDEX_PATH = INVALIDS.joinpath("README.md")

KEYS = [
    "prov_pack",
    "synonym_pack",
    "xref_pack",
]

INVALID_KEY = "invalid_luids"
OBO_PREFIX = "http://purl.obolibrary.org/obo/"


def main():
    """Analyze invalid identifiers."""
    source_agg = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    xref_agg = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for path in RESULTS.glob("*.json"):
        source = path.stem
        for results in json.loads(path.read_text()).values():
            for key in KEYS:
                for node, invalid_xrefs in results[key][INVALID_KEY].items():
                    # node_curie = node.removeprefix(OBO_PREFIX).replace("_", ":")
                    for xref in invalid_xrefs:
                        xref_prefix, xref_identifier = xref.split(":", 1)
                        xref_norm_prefix = bioregistry.normalize_prefix(xref_prefix)
                        source_agg[source][xref_prefix][xref_prefix, xref_identifier].append(node)
                        xref_agg[xref_norm_prefix][source][xref_prefix, xref_identifier].append(
                            node
                        )

    index_text = dedent(
        """\
    # Invalid Identifier Analysis

    This analysis has been conducted across all ontologies listed in the Bioregistry by loading
    them from source with ROBOT, converting to OBO Graph JSON, then looking through all nodes’
    xrefs, nodes’ synonyms’ xrefs, and nodes’ definitions’ xrefs to see which ones make references
    using identifiers that don't validate against patterns in the [Bioregistry](https://bioregistry.io).

    """
    )
    rows = []
    for xref_norm_prefix, inner in xref_agg.items():
        sources = ", ".join(f"[`{source}`](source/{source})" for source in inner)
        total = sum(len(d.values()) for d in inner.values())
        example_source = random.choice(list(inner))
        example_curie = random.choice(list(inner[example_source]))
        example_node = random.choice(list(inner[example_source][example_curie]))
        rows.append(
            (
                f"[`{xref_norm_prefix}`](prefix/{xref_norm_prefix})",
                sources,
                total,
                "`" + ":".join(example_curie) + "`",
                example_node,
            )
        )
    rows = sorted(rows, key=itemgetter(2), reverse=True)
    index_text += tabulate(
        rows,
        headers=["xref_prefix", "sources", "count", "example_xref", "example_node"],
        tablefmt="github",
    )
    INDEX_PATH.write_text(index_text)

    for xref_norm_prefix, xref_inner in tqdm(xref_agg.items(), unit="prefix"):
        xref_name = bioregistry.get_name(xref_norm_prefix)
        xref_path = PREFIXES.joinpath(f"{xref_norm_prefix}.md")
        variants = {
            xref_prefix for xref_inner_2 in xref_inner.values() for xref_prefix, _ in xref_inner_2
        }
        source_text = dedent(
            f"""\
        # [`{xref_norm_prefix}`](https://bioregistry.io/{xref_norm_prefix}): {xref_name}

        This page summarize the different resources that reference `{xref_norm_prefix}`
        but use local unique identifiers that do not match the standard pattern of
        `{bioregistry.get_pattern(xref_norm_prefix)}`. Of the {len(xref_inner):,} resources,
        {len(variants)} variants on the standard prefix were found: {sorted(variants)}.

        """
        )

        for source, inner2 in sorted(xref_inner.items(), key=lambda t: t[0].casefold()):
            repository = bioregistry.get_repository(source)
            repo_text = f" See the [GitHub repository]({repository})." if repository else ""
            source_text += dedent(
                f"""\
            ## `{source}`: {bioregistry.get_name(source)}

            Identifiers for this prefix are given incorrectly in `{source}`.{repo_text}

            """
            )
            rows = []
            for (xref_prefix, xref_identifier), nodes in inner2.items():
                invalid_xref_curie = f"{xref_prefix}:{xref_identifier}"
                if len(nodes) > 5:
                    examples = (
                        ", ".join(
                            f"[{example_node}]({example_node})"
                            for example_node in sorted(nodes)[:5]
                        )
                        + ", ..."
                    )
                else:
                    examples = ", ".join(
                        f"[{example_node}]({example_node})" for example_node in sorted(nodes)
                    )

                rows.append(
                    (
                        f"`{invalid_xref_curie}`",
                        len(nodes),
                        examples,
                    )
                )
            rows = sorted(rows, key=itemgetter(1), reverse=True)
            source_text += tabulate(
                rows,
                headers=["external_xref", "usages_count", "usages"],
                tablefmt="github",
            )
            source_text += "\n\n"

        xref_path.write_text(source_text)

    for source, inner in tqdm(source_agg.items(), unit="source"):
        source_path = SOURCES.joinpath(f"{source}.md")
        repository = bioregistry.get_repository(source)
        repo_text = f" See the [GitHub repository]({repository})." if repository else ""
        source_text = dedent(
            f"""\
        # {source}

        This document details the invalid local unique identifiers used in CURIEs
        for node, synonym, and definition cross-references in `{source}`.{repo_text}


        """
        )

        for xref_prefix, inner2 in sorted(inner.items(), key=lambda t: t[0].casefold()):
            norm_prefix = bioregistry.normalize_prefix(xref_prefix)
            source_text += dedent(
                f"""\
            ## `{xref_prefix}`: {bioregistry.get_name(xref_prefix)}

            Overall, there were {sum(len(nodes) for nodes in inner2.values()):,} invalid
            xrefs to external prefixed with `{xref_prefix}` (standardized to Bioregistry
            prefix [`{norm_prefix}`](https://bioregistry.io/{norm_prefix})) that
            did not match the standard pattern `{bioregistry.get_pattern(xref_prefix)}`.

            """
            )
            rows = []
            for xref_identifier, nodes in inner2.items():
                invalid_xref_curie = f"{xref_prefix}:{xref_identifier}"
                if len(nodes) > 5:
                    examples = (
                        ", ".join(
                            f"[{example_node}]({example_node})"
                            for example_node in sorted(nodes)[:5]
                        )
                        + ", ..."
                    )
                else:
                    examples = ", ".join(
                        f"[{example_node}]({example_node})" for example_node in sorted(nodes)
                    )

                rows.append(
                    (
                        f"`{invalid_xref_curie}`",
                        len(nodes),
                        examples,
                    )
                )
            rows = sorted(rows, key=itemgetter(1), reverse=True)
            source_text += tabulate(
                rows,
                headers=["external_xref", "usages_count", "usages"],
                tablefmt="github",
            )
            source_text += "\n\n"

        source_path.write_text(source_text)


if __name__ == "__main__":
    main()
