"""Analyze invalid identifiers."""

import json
import re
from urllib.parse import urlparse

import bioregistry
from tabulate import tabulate

from oquat.large_scale_analysis import DOCS, RESULTS

INVALIDS = DOCS.joinpath("versions")
INVALIDS.mkdir(exist_ok=True, parents=True)
INDEX_PATH = INVALIDS.joinpath("README.md")

#: Official regex for semantic versions from
#: https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)(\.(0|[1-9]\d*))?(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"  # noqa:E501
)
#: Regular expression for ISO 8601 compliant date in YYYY-MM-DD format
DATE_PATTERN = re.compile(r"^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$")


def main():
    """Analyze invalid identifiers."""
    full_analysis_rows = []
    obo_analysis_rows = []
    for path in RESULTS.glob("*.json"):
        source = path.stem
        resource = bioregistry.get_resource(source)
        obo_prefix = None if resource is None else resource.get_obofoundry_prefix()

        for i, graph in json.loads(path.read_text()).items():
            if "import" in i:
                continue
            version = graph.get("version")
            if version:
                version = version.replace("\n", " ")
            version_iri = graph.get("version_iri")
            if not version or not version_iri:
                version_in_version_iri = ""
            elif version in version_iri:
                version_in_version_iri = "✅"
            else:
                version_in_version_iri = "⭕"
            full_analysis_rows.append((source, i, version, version_iri, version_in_version_iri))

            if obo_prefix and i == f"http://purl.obolibrary.org/obo/{obo_prefix.lower()}.owl":
                # This is the "canonical" resource
                if version_iri:

                    if (
                        f"http://purl.obolibrary.org/obo/{obo_prefix.lower()}/releases/"
                        in version_iri
                    ):
                        standard_viri = "✅"
                    else:
                        standard_viri = "⭕"
                    if _contains_semver(version_iri) or _contains_date(version_iri):
                        versioned_version_iri = "✅"
                    else:
                        versioned_version_iri = "⭕"
                else:
                    standard_viri = ""
                    versioned_version_iri = ""

                obo_analysis_rows.append(
                    (
                        f"[{source}](http://obofoundry.org/ontology/{source})",
                        version_iri,
                        versioned_version_iri,
                        standard_viri,
                        version,
                        version_in_version_iri,
                    )
                )

    obo_headers = [
        "source",
        "version_iri",
        "version_iri_has_version",
        "version_iri_is_standard",
        "graph_version",
        "version_in_iri",
    ]
    full_headers = ["source", "graph_id", "graph_version", "graph_version_iri", "version_in_iri"]
    INDEX_PATH.write_text(
        f"""
# OBO Analysis

This analysis shows which OBO Foundry ontologies are conforming to
required and suggested practices in versioning of ontologies.

{tabulate(sorted(obo_analysis_rows), tablefmt="github", headers=obo_headers)}

# Full Analysis

This analysis is extended to _all_ ontologies.

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


if __name__ == "__main__":
    main()
