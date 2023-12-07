"""Analyze unknown prefixes."""

import json
import random
from collections import defaultdict
from operator import itemgetter

from bioregistry.utils import norm
from tabulate import tabulate
from tqdm import tqdm

from oquat.api import AnalysisResults, ResultPack
from oquat.large_scale_analysis import DOCS, RESULTS, url_md

UNKNOWNS = DOCS.joinpath("unknowns")
UNKNOWNS.mkdir(exist_ok=True, parents=True)
SOURCES = UNKNOWNS.joinpath("source")
SOURCES.mkdir(exist_ok=True, parents=True)
PREFIXES = UNKNOWNS.joinpath("prefix")
PREFIXES.mkdir(exist_ok=True, parents=True)

KEYS = [
    "prov_pack",
    "synonym_pack",
    "xref_pack",
]


def main() -> None:
    """Analyze unknown prefixes."""
    prefix_agg = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))  # type:ignore
    source_agg = defaultdict(dict)  # type:ignore
    for path in RESULTS.glob("*.json"):
        source = path.stem
        analysis_results = AnalysisResults.parse_obj(json.loads(path.read_text()))
        for results in analysis_results.results.values():
            for key in KEYS:
                pack: ResultPack = getattr(results, key)
                for unknown_prefix, node_to_curie in pack.unknown_prefixes.items():
                    if (
                        " " in unknown_prefix
                        or "www." in unknown_prefix
                        or len(unknown_prefix) > 20
                    ):
                        continue  # lots of garbage
                    source_agg[source][unknown_prefix] = node_to_curie

                    unknown_prefix_norm = norm(unknown_prefix)
                    unknown_prefix_norm = (
                        unknown_prefix_norm.replace("/", "_")
                        .replace(".", "_")
                        .replace("[", "")
                        .replace("(", "")
                        .replace(")", "")
                    )
                    for node, curie in node_to_curie.items():
                        prefix_agg[unknown_prefix_norm][source][curie].add(node)

    source_it = tqdm(source_agg.items(), desc="Generating source pages", unit="source")
    for source, counts in source_it:
        source_path = SOURCES.joinpath(f"{source}.md")
        source_text = f"# {source}\n\n"
        for unknown_prefix, node_to_curie in counts.items():
            dd = defaultdict(set)
            for node, curie in node_to_curie.items():
                dd[curie].add(node)
            rows = [
                (
                    curie,
                    len(nodes),
                    ", ".join(url_md(node) for node in sorted(nodes)[:5])
                    + ("" if len(nodes) < 5 else ", ..."),
                )
                for curie, nodes in dd.items()
            ]
            rows = sorted(
                rows,
                key=itemgetter(1),
                reverse=True,
            )
            source_text += f"""\
## `{unknown_prefix}`

There are {len(rows)} usages of `{unknown_prefix}` in `{source}`.
If you are knowledgeable about this prefix, please consider submitting a new prefix
request to the Bioregistry [here](https://github.com/biopragmatics/bioregistry/issues/new?\
assignees=cthoyt&labels=New%2CPrefix&template=new-prefix.yml&title=%5BResource%5D%3A%20{unknown_prefix}).

"""
            table_text = (
                tabulate(
                    rows,
                    headers=["curie", "usages", "nodes"],
                    tablefmt="github",
                )
                + "\n\n"
            )

            if len(rows) < 20:
                source_text += table_text
            else:
                source_text += f"""\
<details>
<summary>Click to expand the `{unknown_prefix}` table</summary>

{table_text}</details>

"""

        source_path.write_text(source_text)

    summary_rows = []
    prefix_it = tqdm(prefix_agg.items(), desc="Generating unknown prefix pages", unit="prefix")
    for unknown_prefix, source_to_curie_to_nodes in prefix_it:
        if not unknown_prefix:
            continue
        prefix_it.set_postfix(prefix=unknown_prefix)
        prefix_agg_str = ", ".join(
            f"[`{source}`](source/{source})" for source in sorted(source_to_curie_to_nodes)
        )
        unique_usages = sum(len(v) for v in source_to_curie_to_nodes.values())
        total_usages = sum(
            len(nodes)
            for curie_to_nodes in source_to_curie_to_nodes.values()
            for nodes in curie_to_nodes.values()
        )
        example_source = random.choice(list(source_to_curie_to_nodes))
        example_curie = random.choice(list(source_to_curie_to_nodes[example_source]))
        example_node = random.choice(list(source_to_curie_to_nodes[example_source][example_curie]))

        prefix_text = f"# `{unknown_prefix}`\n\n"
        for source, curie_to_nodes in source_to_curie_to_nodes.items():
            rows = [
                (
                    curie,
                    len(nodes),
                    ", ".join(url_md(node) for node in sorted(nodes)[:5])
                    + ("" if len(nodes) < 5 else ", ..."),
                )
                for curie, nodes in curie_to_nodes.items()
            ]
            rows = sorted(
                rows,
                key=itemgetter(1),
                reverse=True,
            )

            prefix_text += f"## {source}\n\n"
            prefix_text += tabulate(
                rows,
                headers=["curie", "usages", "nodes"],
                tablefmt="github",
            )
            prefix_text += "\n\n"

        prefix_path = PREFIXES.joinpath(f"{unknown_prefix}.md")
        prefix_path.write_text(prefix_text)

        summary_rows.append(
            (
                f"[`{unknown_prefix}`](prefix/{unknown_prefix})",
                prefix_agg_str,
                unique_usages,
                total_usages,
                f"[{example_node}]({example_node})",
                f"`{example_curie}`",
            )
        )

    summary_rows = sorted(
        summary_rows,
        key=itemgetter(2),
        reverse=True,
    )

    text = """\
# Unknown Prefix Analysis

This analysis has been conducted across all ontologies listed in the Bioregistry
by loading them from source with ROBOT, converting to OBO Graph JSON, then looking
through all nodes' xrefs, nodes' synonyms' xrefs, and nodes' definitions' xrefs
to see which ones make references using prefixes that aren't recognized by the
Bioregistry.

There's an incredible amount of garbage that was heuristically removed from this
list by removing all references containing a space in their prefix as well as
any prefix over 25 characters long.

"""

    text += tabulate(
        summary_rows,
        headers=[
            "prefix",
            "sources",
            "unique_usages",
            "total_usages",
            "example_node",
            "example_xref_curie",
        ],
        tablefmt="github",
    )
    UNKNOWNS.joinpath("README.md").write_text(text)


if __name__ == "__main__":
    main()
