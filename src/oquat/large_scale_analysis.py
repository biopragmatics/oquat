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
from tqdm import tqdm

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
]

HERE = Path(__file__).parent.resolve()
TEMPLATES = HERE.joinpath("templates")
ROOT = HERE.parent.parent.resolve()
DOCS = ROOT.joinpath("docs")
RESULTS = ROOT.joinpath("results")
FAILURES_PATH = RESULTS.joinpath("failures.txt")

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

    def _failure(text):
        secho(text, fg="red")
        failures.append(text)

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
            failure_text = f"{prefix} has an unhanded suffix in its OWL URL: {owl_url}"
            secho(failure_text, fg="red")
            failures.append(failure_text)
            continue
        if json_url is None and owl_url is None and not obo_url.endswith(".obo"):
            failure_text = f"{prefix} does not have an OBO URL: {obo_url}"
            secho(failure_text, fg="red")
            failures.append(failure_text)
            continue
        it.set_postfix(prefix=prefix)
        analysis_path = RESULTS.joinpath(prefix).with_suffix(".json")
        if analysis_path.is_file() and not force:
            result = {k: Results(**v) for k, v in json.loads(analysis_path.read_text()).items()}
        else:
            result = None
            try:
                analysis_results = analyze_by_prefix(
                    prefix, iri_filter=iri_filter or CUSTOM_FILTERS.get(prefix)
                )
            except urllib.error.URLError:
                failure_text = f"{prefix} could not be downloaded"
                _failure(failure_text)
            except subprocess.CalledProcessError:
                failure_text = f"{prefix} could not be parsed by ROBOT"
                _failure(failure_text)
            except TypeError as e:
                failure_text = f"{prefix} unknown error during parsing: {e}"
                _failure(failure_text)
                raise
            except MissingGraphIRI:
                failure_text = f"{prefix} missing graph ID"
                _failure(failure_text)
            except NoParsableURIs:
                failure_text = f"{prefix} None of the URIs could be parsed"
                _failure(failure_text)
            else:
                result = analysis_results.results

            # secho(f"{prefix} writing results to {analysis_path}")
            if result is not None:
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
        if result is None:
            pass
        # elif result.unknown_prefixes or result.malformed_curies:
        #     secho(f"prefix: {prefix} has issues", fg="yellow")
        # it.write(result.as_str())

    FAILURES_PATH.write_text("\n".join(failures))
    # template = environment.get_template("invalid_xrefs.md")
    # OUTPUT.write_text(template.render(results=results, bioregistry=bioregistry))


if __name__ == "__main__":
    lsa()
