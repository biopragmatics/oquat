import json
import random
from collections import Counter, defaultdict
from operator import itemgetter

from tabulate import tabulate

from oquat.large_scale_analysis import RESULTS

KEYS = [
    ("prov_pack", "Provenance"),
    ("synonym_pack", "Synoynms"),
    ("xref_pack", "Xrefs"),
]


def main():
    go_data = json.loads(RESULTS.joinpath("go.json").read_text())
    for key, label in KEYS:
        dd = defaultdict(list)
        for graph_id, graph in go_data.items():
            for unknown_prefix, usages in graph[key]["unknown_prefixes"].items():
                if "goc" in unknown_prefix.lower():
                    continue
                for node, value in usages.items():
                    dd[value].append(
                        node.removeprefix("http://purl.obolibrary.org/obo/").replace("_", ":")
                    )

        if not dd:
            continue
        print(f"## {label}\n")
        rows = [
            (value, len(terms), ", ".join(random.choices(list(terms), k=5)))
            for value, terms in dd.items()
        ]
        rows = sorted(rows, key=itemgetter(1), reverse=True)
        print(
            tabulate(
                rows,
                headers=["term", "usages", "examples"],
                tablefmt="github",
            )
        )
        print()


if __name__ == "__main__":
    main()
