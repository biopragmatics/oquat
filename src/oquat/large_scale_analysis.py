# -*- coding: utf-8 -*-

"""Automate analysis on all ontologies listed in the Bioregistry."""

import json
import subprocess
import urllib.error
from pathlib import Path
from typing import Optional

import bioregistry
import click
import jinja2
from more_click import force_option, verbose_option
from tabulate import tabulate
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from .api import (
    SKIP_PREFIXES,
    MissingGraphIRI,
    NoParsableURIs,
    Results,
    analyze_by_prefix,
    extended_encoder,
    secho,
)

__all__ = [
    "lsa",
    "lsa_artifacts",
]

HERE = Path(__file__).parent.resolve()
TEMPLATES = HERE.joinpath("templates")
ROOT = HERE.parent.parent.resolve()
DOCS = ROOT.joinpath("docs")
RESULTS = ROOT.joinpath("results")
FAILURES_PATH = DOCS.joinpath("failures.md")

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES),
    trim_blocks=True,
    autoescape=True,
)

CUSTOM_FILTERS = {"efo": "http://www.ebi.ac.uk/efo/EFO_"}
EXTENSION_EXCEPTIONS = {
    "http://www.w3.org/ns/prov-o-20130430",  # this is pointing to a RDF file
}


@click.command()
@force_option
@click.option("--minimum")
@verbose_option
def lsa(force: bool, minimum: Optional[str]):
    """Run large-scale ontology analysis."""
    with logging_redirect_tqdm():
        _lsa(force=force, minimum=minimum)


@click.command()
@verbose_option
def lsa_artifacts():
    """Generate large-scale ontology analyis artifacts."""
    _generate_artifacts()


def _lsa(force: bool, minimum: Optional[str]):
    rows = sorted(
        (
            prefix,
            CUSTOM_FILTERS.get(prefix) or bioregistry.get_obofoundry_uri_prefix(prefix),
            bioregistry.get_owl_download(prefix),
            bioregistry.get_json_download(prefix),
            bioregistry.get_obo_download(prefix),
        )
        for prefix, resource in bioregistry.read_registry().items()
        if prefix not in SKIP_PREFIXES
        and (not minimum or minimum <= prefix)
        and not resource.no_own_terms
    )
    results = []
    failures = []

    def _failure(*, prefix: str, text: str, fg: str = "red") -> None:
        _text = f"{prefix} - {text}"
        secho(_text, fg=fg)
        failures.append((prefix, text))

    tqdm.write(f"got info on {len(rows)} prefixes")
    it = tqdm(rows)
    for prefix, iri_filter, owl_url, json_url, obo_url in it:
        if owl_url is None and json_url is None and obo_url is None:
            continue
        if (
            json_url is None
            and owl_url
            and all(not owl_url.endswith(suffix) for suffix in [".owl", ".obo", ".rdf", ".xml"])
            and owl_url not in EXTENSION_EXCEPTIONS
            and not owl_url.startswith("https://cropontology.org/ontology/")
        ):
            _failure(prefix=prefix, text=f"Unhanded suffix in its OWL URL: {owl_url}")
            continue
        if json_url is None and owl_url is None and not obo_url.endswith(".obo"):
            failure_text = f"Invalid OBO URL: {obo_url}"
            _failure(prefix=prefix, text=failure_text)
            continue

        analysis_path = RESULTS.joinpath(prefix).with_suffix(".json")
        if analysis_path.is_file() and not force:
            tqdm.write(f"loading results from {analysis_path}")
            result = {k: Results(**v) for k, v in json.loads(analysis_path.read_text()).items()}
        else:
            _iri_filter = iri_filter or CUSTOM_FILTERS.get(prefix)
            text = f"analyzing {prefix} with IRI filter {_iri_filter}"
            if bioregistry.is_deprecated(prefix):
                text = f"{text} (⚠️  deprecated)"
            tqdm.write(text)
            result = None
            try:
                analysis_results = analyze_by_prefix(prefix, iri_filter=_iri_filter)
            except urllib.error.URLError:
                failure_text = "Could not be downloaded"
                _failure(prefix=prefix, text=failure_text)
            except subprocess.CalledProcessError:
                failure_text = "ROBOT could not parse"
                _failure(prefix=prefix, text=failure_text)
            except MissingGraphIRI:
                failure_text = "Missing graph ID"
                _failure(prefix=prefix, text=failure_text)
            except NoParsableURIs:
                failure_text = "None of the URIs could be parsed"
                _failure(prefix=prefix, text=failure_text)
            except (ValueError, TypeError, RuntimeError) as e:
                failure_text = f"General error: {e}"
                _failure(prefix=prefix, text=failure_text)
            else:
                result = analysis_results.results
                for message in analysis_results.messages:
                    secho(f"> {message}", fg="yellow")

            # secho(f"{prefix} writing results to {analysis_path}")
            if not result:
                _failure(prefix=prefix, text="No parsable graphs")
            else:
                tqdm.write(f"writing {prefix} to {analysis_path}")
                analysis_path.write_text(
                    json.dumps(
                        result,
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=False,
                        default=extended_encoder,
                    )
                )

        results.append((prefix, result))

    FAILURES_PATH.write_text(
        "# Failures\n\n"
        + tabulate(failures, headers=["prefix", "message"], tablefmt="github")
        + "\n"
    )
    _generate_artifacts()


def _generate_artifacts():
    from . import analyze_invalids, analyze_unknowns, analyze_versions

    analyze_invalids.main()
    analyze_unknowns.main()
    analyze_versions.main()


OBO_PREFIX = "http://purl.obolibrary.org/obo/"


def url_md(s: str) -> str:
    """Convert a URL to markdown link."""
    if s.startswith(OBO_PREFIX):
        short = s[len(OBO_PREFIX) :].replace("_", ":")
        return f"[{short}]({s})"
    if s.startswith("http://www.ebi.ac.uk/efo/EFO_"):
        short = s[len("http://www.ebi.ac.uk/efo/") :].replace("_", ":")
        return f"[{short}]({s})"
    return f"[{s}]({s})"


if __name__ == "__main__":
    lsa()
