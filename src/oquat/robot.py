"""A wrapper around ROBOT functionality.

.. seealso:: https://robot.obolibrary.org
"""

import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from subprocess import check_output
from typing import Any, Literal, Tuple, Union

from .struct.obograph import Graphs

__all__ = [
    "robot_parse_json_local",
    "robot_parse_json_remote",
]


def robot_parse_json_local(
    owl_path: Union[str, Path],
    json_path: Union[None, str, Path] = None,
) -> Tuple[Graphs, Any]:
    """Convert a local OWL file to a JSON file."""
    return robot_parse_json(flag="-i", input_path=owl_path, output_path=json_path)


def robot_parse_json_remote(
    owl_iri: str,
    json_path: Union[None, str, Path] = None,
) -> Tuple[Graphs, Any]:
    """Convert a local OWL file to a JSON file."""
    return robot_parse_json(flag="-I", input_path=owl_iri, output_path=json_path)


def robot_parse_json(
    flag: Literal["-i", "-I"],
    input_path: Union[str, Path],
    output_path: Union[None, str, Path] = None,
) -> Tuple[Graphs, Any]:
    """Convert a local OWL file to a JSON file"""
    with _path_context(output_path) as path:
        args = ["robot", "convert", flag, str(input_path), "-o", str(path), "--format", "json"]
        ret = check_output(args, cwd=os.path.dirname(__file__))  # noqa:S603
        messages = ret.decode().strip()
        data = json.loads(path.read_text())
        return data, messages


@contextmanager
def _path_context(path: Union[None, str, Path], name: str = "output.json"):
    if path is not None:
        yield Path(path).resolve()
    else:
        with tempfile.TemporaryDirectory() as directory:
            yield Path(directory).joinpath(name)
