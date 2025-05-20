"""Command line interface for :mod:`oquat`."""

from __future__ import annotations

import logging

import click

from . import api, large_scale_analysis

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)


@click.group()
@click.version_option()
def main():
    """CLI for oquat."""


main.add_command(api.analyze)
main.add_command(large_scale_analysis.lsa)
main.add_command(large_scale_analysis.lsa_artifacts)

if __name__ == "__main__":
    main()
