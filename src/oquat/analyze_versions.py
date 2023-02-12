"""Analyze invalid identifiers."""

import json
import re
from urllib.parse import urlparse

import bioregistry
from tabulate import tabulate
from tqdm import tqdm

from oquat.large_scale_analysis import DOCS, RESULTS

INVALIDS = DOCS.joinpath("versions")
INVALIDS.mkdir(exist_ok=True, parents=True)
INDEX_PATH = INVALIDS.joinpath("README.md")

#: Official regex for semantic versions from
#: https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)(\.(0|[1-9]\d*))?(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    # noqa:E501
)
#: Regular expression for ISO 8601 compliant date in YYYY-MM-DD format
DATE_PATTERN = re.compile(r"^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$")


def main():
    """Analyze invalid identifiers."""
    full_analysis_rows = []
    obo_analysis_rows = []
    for path in RESULTS.glob("*.json"):
        prefix = path.stem
        resource = bioregistry.get_resource(prefix)
        obo_prefix = None if resource is None else resource.get_obofoundry_prefix()

        for graph_iri, graph in json.loads(path.read_text()).items():
            if "import" in graph_iri:
                continue
            graph_version = graph.get("version", "")
            if graph_version:
                graph_version = graph_version.replace("\n", " ")
            version_iri = graph.get("version_iri", "")

            if obo_prefix:
                if graph_iri != f"http://purl.obolibrary.org/obo/{obo_prefix.lower()}.owl":
                    # skip this since there are potentially many graphs contained for a given OBO prefix
                    continue
                if version_iri:
                    version_length, version_type, v = _parse_version_iri(version_iri, obo_prefix)
                    standard_viri = "✅" if version_length else "⭕"
                    versioned_version_iri = "✅" if version_type else "⭕"
                    if graph_version:
                        version_in_version_iri = "✅" if graph_version == v else "⭕"
                    else:
                        version_in_version_iri = ""
                else:
                    standard_viri = ""
                    versioned_version_iri = ""
                    version_in_version_iri = ""

                obo_analysis_rows.append(
                    (
                        f"[{prefix}](http://obofoundry.org/ontology/{prefix})",
                        version_iri,
                        versioned_version_iri,
                        standard_viri,
                        graph_version,
                        version_in_version_iri,
                    )
                )
            else:
                if not graph_version or not version_iri:
                    version_in_version_iri = ""
                elif graph_version in version_iri:
                    version_in_version_iri = "✅"
                else:
                    version_in_version_iri = "⭕"

            full_analysis_rows.append(
                (prefix, graph_iri, graph_version, version_iri, version_in_version_iri)
            )

    n_has_iri = sum(bool(row[1]) for row in obo_analysis_rows)
    n_iri_has_version = sum(row[2] == "✅" for row in obo_analysis_rows)
    n_iri_is_standard = sum(row[3] == "✅" for row in obo_analysis_rows)
    n_has_version = sum(bool(row[4]) for row in obo_analysis_rows)
    n_version_in_iri = sum(row[5] == "✅" for row in obo_analysis_rows)
    n_obo = len(obo_analysis_rows)

    obo_headers = [
        "source",
        "version iri",
        "version iri has version",
        "version iri is standard",
        "version",
        "version in iri",
    ]
    full_headers = ["source", "graph_id", "graph_version", "graph_version_iri", "version_in_iri"]
    INDEX_PATH.write_text(
        f"""\
# OBO Analysis

This analysis shows which OBO Foundry ontologies are conforming to
required and suggested practices in versioning of ontologies. This
table has the following columns:

1. The prefix of the ontology
2. Has a version IRI ({n_has_iri}/{n_obo}, {n_has_iri / n_obo:.1%})
3. Has a version IRI that contains either a semantic version string or `YYYY-MM-DD` date version string
   ({n_iri_has_version}/{n_obo}, {n_iri_has_version / n_obo:.1%})
4. Has a version IRI that follows the standard pattern
   `http://purl.obolibrary.org/obo/<prefix>/releases/<trailing stuff>` or
   `http://purl.obolibrary.org/obo/<prefix>/<trailing stuff>`
   ({n_iri_is_standard}/{n_obo}, {n_iri_is_standard / n_obo:.1%})
5. Has a version annotated with `http://www.w3.org/2002/07/owl#versionInfo`
   ({n_has_version}/{n_obo}, {n_has_version / n_obo:.1%})
6. Has a version that appears in the version IRI
   ({n_version_in_iri}/{n_obo}, {n_version_in_iri / n_obo:.1%})

{tabulate(sorted(obo_analysis_rows), tablefmt="github", headers=obo_headers)}

# Full Analysis

This analysis is extended to _all_ ontologies, each of which potentially has
multiple graphs due to imports.

{tabulate(full_analysis_rows, tablefmt="github", headers=full_headers)}
    """
    )


def _contains_semver(iri: str) -> bool:
    """Return if the IRI contains a semantic version substring."""
    return _match_any_part(iri, SEMVER_PATTERN)


def _contains_date(iri: str) -> bool:
    return _match_any_part(iri, DATE_PATTERN)


def _match_any_part(iri, pattern):
    parse_result = urlparse(iri)
    return any(bool(pattern.match(part)) for part in parse_result.path.split("/"))


def _parse_version_iri(version_iri: str, obo_prefix: str):
    obo_prefix = obo_prefix.lower()
    parts = [
        ("long", f"http://purl.obolibrary.org/obo/{obo_prefix}/releases/"),
        ("short", f"http://purl.obolibrary.org/obo/{obo_prefix}/"),
    ]
    for version_type, version_iri_prefix in parts:
        if not version_iri.startswith(version_iri_prefix):
            continue
        try:
            version, filename = version_iri[len(version_iri_prefix) :].split("/", 1)
        except ValueError:
            tqdm.write(f"[{obo_prefix}] issue parsing IRI back-half: {version_iri}")
            return None, None, None
        if not any(
            filename.startswith(f"{obo_prefix}.{ext}") for ext in ("json", "owl", "obo", "ofn")
        ):
            return None, None, None
        if SEMVER_PATTERN.fullmatch(version):
            version_type = "semver"
        elif DATE_PATTERN.fullmatch(version):
            version_type = "date"
        else:
            version_type = None
        return version_type, version_type, version
    return None, None, None


if __name__ == "__main__":
    main()
