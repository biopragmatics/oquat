import pickle
import subprocess
import urllib.error
from pathlib import Path
from typing import Optional

import bioregistry
import click
import jinja2
import pystow
from more_click import force_option
from tqdm import tqdm

from .api import SKIP_PREFIXES, check_prefix

__all__ = [
    "main",
]

HERE = Path(__file__).parent.resolve()
TEMPLATES = HERE.joinpath("templates")
OUTPUT = HERE.joinpath("output.md")
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES),
    trim_blocks=True,
)


def secho(s, fg=None):
    tqdm.write(click.style(s, fg=fg))


CUSTOM_FILTERS = {
    "efo": "http://www.ebi.ac.uk/efo/EFO_"
}


@click.command()
@force_option
@click.option('--inclusive', is_flag=True, help="Include non-OBO and less well annotated ontologies")
@click.option('--minimum')
def main(force: bool, inclusive: bool, minimum: Optional[str]):
    rows = sorted(
        (
            prefix,
            bioregistry.get_obofoundry_uri_prefix(prefix),
            bioregistry.get_owl_download(prefix),
            bioregistry.get_json_download(prefix),
        )
        for prefix in bioregistry.read_registry()
        if prefix not in SKIP_PREFIXES and (not minimum or minimum <= prefix)
    )
    results = []
    tqdm.write(f'got info on {len(rows)} prefixes')
    it = tqdm(rows)
    for prefix, iri_filter, owl_url, json_url in it:
        iri_filter = CUSTOM_FILTERS.get(prefix, iri_filter)
        if not inclusive and iri_filter is None:
            continue
        if json_url is None:
            if owl_url is None:
                continue
            if not owl_url.endswith(".owl"):
                secho(f"{prefix} does not have an OWL URL: {owl_url}", fg="red")
                continue
        it.set_postfix(prefix=prefix)
        analysis_path = pystow.join("bio", "obofoundry", prefix, name="analysis.pkl")
        if analysis_path.is_file() and not force:
            result = pickle.loads(analysis_path.read_bytes())
        else:
            try:
                result = check_prefix(prefix, iri_filter=iri_filter or CUSTOM_FILTERS.get(prefix))
            except urllib.error.URLError:
                secho(f"{prefix} could not be downloaded", fg="red")
                result = None
            except subprocess.CalledProcessError:
                secho(f"{prefix} could not be parsed by ROBOT", fg="red")
                result = None
            except TypeError as e:
                secho(f"{prefix} unknown error during parsing: {e}", fg="red")
                result = None

            # secho(f"{prefix} writing results to {analysis_path}")
            analysis_path.write_bytes(pickle.dumps(result))

        results.append((prefix, result))
        if result is None:
            pass
        elif result.unknown_prefixes or result.malformed_curies:
            secho(f"prefix: {prefix} has issues", fg="yellow")
            # it.write(result.as_str())

    template = environment.get_template("invalid_xrefs.md")
    OUTPUT.write_text(template.render(results=results, bioregistry=bioregistry))


if __name__ == '__main__':
    main()
