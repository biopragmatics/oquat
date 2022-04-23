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
from more_click import force_option
from tqdm import tqdm

from .api import SKIP_PREFIXES, MissingGraphIRI, Results, analyze_by_prefix, extended_encoder

__all__ = [
    "main",
]

HERE = Path(__file__).parent.resolve()
TEMPLATES = HERE.joinpath("templates")
ROOT = HERE.parent.parent.resolve()
RESULTS = ROOT.joinpath("results")
FAILURES_PATH = RESULTS.joinpath("failures.txt")

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES),
    trim_blocks=True,
    autoescape=True,
)


def secho(s: str, fg=None) -> None:
    """Write text in tqdm with :func:`click.style`."""
    tqdm.write(click.style(s, fg=fg))


CUSTOM_FILTERS = {"efo": "http://www.ebi.ac.uk/efo/EFO_"}


@click.command()
@force_option
@click.option(
    "--inclusive", is_flag=True, help="Include non-OBO and less well annotated ontologies"
)
@click.option("--minimum")
def main(force: bool, inclusive: bool, minimum: Optional[str]):
    """Run large-scale ontology analysis."""
    rows = sorted(
        (
            prefix,
            bioregistry.get_obofoundry_uri_prefix(prefix),
            bioregistry.get_owl_download(prefix),
            bioregistry.get_json_download(prefix),
        )
        for prefix, resource in bioregistry.read_registry().items()
        if prefix not in SKIP_PREFIXES
        and (not minimum or minimum <= prefix)
        and not resource.no_own_terms
    )
    results = []
    failures = []
    tqdm.write(f"got info on {len(rows)} prefixes")
    it = tqdm(rows)
    for prefix, iri_filter, owl_url, json_url in it:
        iri_filter = CUSTOM_FILTERS.get(prefix, iri_filter)
        if not inclusive and iri_filter is None:
            continue
        if json_url is None:
            if owl_url is None:
                failure_text = f"{prefix} does not have a download URL: {owl_url}"
                failures.append(failure_text)
                continue
            if not owl_url.endswith(".owl"):
                failure_text = f"{prefix} does not have an OWL URL: {owl_url}"
                secho(failure_text, fg="red")
                failures.append(failure_text)
                continue
        it.set_postfix(prefix=prefix)
        analysis_path = RESULTS.joinpath(prefix).with_suffix(".json")
        if analysis_path.is_file() and not force:
            result = {k: Results(**v) for k, v in json.loads(analysis_path.read_text()).items()}
        else:
            try:
                result = analyze_by_prefix(
                    prefix, iri_filter=iri_filter or CUSTOM_FILTERS.get(prefix)
                )
            except urllib.error.URLError:
                failure_text = f"{prefix} could not be downloaded"
                secho(failure_text, fg="red")
                failures.append(failure_text)
                result = None
            except subprocess.CalledProcessError:
                failure_text = f"{prefix} could not be parsed by ROBOT"
                secho(failure_text, fg="red")
                failures.append(failure_text)
                result = None
            except TypeError as e:
                failure_text = f"{prefix} unknown error during parsing: {e}"
                secho(failure_text, fg="red")
                failures.append(failure_text)
                result = None
            except MissingGraphIRI:
                failure_text = f"{prefix} missing graph ID"
                secho(failure_text, fg="red")
                failures.append(failure_text)
                result = None

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
    main()
