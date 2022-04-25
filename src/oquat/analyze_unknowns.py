"""Analyze unknown prefixes."""

import json
import random
from collections import defaultdict
from operator import itemgetter

from tabulate import tabulate
from tqdm import tqdm

from oquat.large_scale_analysis import DOCS, RESULTS

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


def main():
    """Analyze unknown prefixes."""
    prefix_agg = defaultdict(dict)
    source_agg = defaultdict(dict)
    for path in RESULTS.glob("*.json"):
        source = path.stem
        for results in json.loads(path.read_text()).values():
            for key in KEYS:
                for unknown_prefix, usages in results[key]["unknown_prefixes"].items():
                    if (
                        " " in unknown_prefix
                        or "www." in unknown_prefix
                        or len(unknown_prefix) > 20
                    ):
                        continue  # lots of garbage
                    prefix_agg[unknown_prefix][source] = usages
                    source_agg[source][unknown_prefix] = usages

    source_it = tqdm(source_agg.items(), desc="Generating source pages", unit="source")
    for source, counts in source_it:
        source_path = SOURCES.joinpath(f"{source}.md")
        source_text = f"# {source}\n\n"
        for unknown_prefix, usages in counts.items():
            dd = defaultdict(set)
            for node, curie in usages.items():
                dd[curie].add(
                    node.removeprefix("http://purl.obolibrary.org/obo/").replace("_", ":")
                )
            rows = [
                (
                    curie,
                    len(nodes),
                    ", ".join(
                        f"[{node}](https://bioregistry.io/{node})" for node in sorted(nodes)[:15]
                    )
                    + ("" if len(nodes) < 15 else ", ..."),
                )
                for curie, nodes in dd.items()
            ]
            rows = sorted(
                rows,
                key=itemgetter(1),
                reverse=True,
            )
            source_text += f"## `{unknown_prefix}`\n\n"
            source_text += tabulate(
                rows,
                headers=["curie", "usages", "nodes"],
                tablefmt="github",
            )
            source_text += "\n\n"

        source_path.write_text(source_text)

    summary_rows = []
    prefix_it = tqdm(prefix_agg.items(), desc="Generating unknown prefix pages", unit="prefix")
    for unknown_prefix, counts in prefix_it:
        unknown_prefix_norm = (
            unknown_prefix.replace("/", "_")
            .replace(".", "_")
            .replace("[", "")
            .replace("(", "")
            .replace(")", "")
        )
        if not unknown_prefix_norm:
            continue

        prefix_it.set_postfix(prefix=unknown_prefix)
        prefix_agg = ", ".join(f"[`{source}`](source/{source})" for source in sorted(counts))
        total_count = sum(len(v) for v in counts.values())
        example_source = random.choice(list(counts))
        example_key = random.choice(list(counts[example_source]))
        example_curie = counts[example_source][example_key]

        prefix_text = f"# `{unknown_prefix}`\n\n"
        for source, usages in counts.items():
            # from rich import print
            # print(usages)
            # raise
            dd = defaultdict(set)
            for node, curie in usages.items():
                dd[curie].add(
                    node.removeprefix("http://purl.obolibrary.org/obo/").replace("_", ":")
                )
            rows = [
                (
                    curie,
                    len(nodes),
                    ", ".join(
                        f"[{node}](https://bioregistry.io/{node})" for node in sorted(nodes)[:15]
                    )
                    + ("" if len(nodes) < 15 else ", ..."),
                )
                for curie, nodes in dd.items()
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

        prefix_path = PREFIXES.joinpath(f"{unknown_prefix_norm}.md")
        prefix_path.write_text(prefix_text)

        summary_rows.append(
            (
                f"[`{unknown_prefix}`](prefix/{unknown_prefix_norm})",
                prefix_agg,
                total_count,
                f"[{example_key}]({example_key})",
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
        headers=["prefix", "sources", "count", "example_key", "example_curie"],
        tablefmt="github",
    )
    UNKNOWNS.joinpath("index.md").write_text(text)


if __name__ == "__main__":
    main()
