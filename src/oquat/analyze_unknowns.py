"""Analyze unknown prefixes."""

import json
import random
from collections import defaultdict
from operator import itemgetter

from tabulate import tabulate

from oquat.large_scale_analysis import DOCS, RESULTS

KEYS = [
    "prov_pack",
    "synonym_pack",
    "xref_pack",
]


def main():
    """Analyze unknown prefixes."""
    sources = defaultdict(dict)
    for path in RESULTS.glob("*.json"):
        name = path.stem
        for results in json.loads(path.read_text()).values():
            for key in KEYS:
                for unknown_prefix, usages in results[key]["unknown_prefixes"].items():
                    if " " in unknown_prefix or len(unknown_prefix) > 20:
                        continue  # lots of garbage
                    sources[unknown_prefix][name] = usages

    rows = []
    for unknown_prefix, counts in sources.items():
        sources = ",".join(sorted(counts))
        total_count = sum(len(v) for v in counts.values())
        example_source = random.choice(list(counts))
        example_key = random.choice(list(counts[example_source]))
        example_value = counts[example_source][example_key]
        rows.append(
            (
                unknown_prefix,
                sources,
                total_count,
                example_key,
                example_value,
            )
        )
    rows = sorted(
        rows,
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
        rows,
        headers=["prefix", "sources", "count", "example_key", "example_value"],
        tablefmt="github",
    )
    DOCS.joinpath("unknowns.md").write_text(text)


if __name__ == "__main__":
    main()
