"""Data structures for representing OBO Graphs.

.. seealso:: https://github.com/geneontology/obographs
"""

from typing import Any, TypedDict

__all__ = ["Edge", "Property", "Meta", "Graph", "Graphs"]


class Edge(TypedDict):
    """Represents an edge in an OBO Graph."""

    sub: str
    pred: str
    obj: str


class Property(TypedDict):
    """Represent a property inside a metadata element."""

    pred: str
    val: str


class Meta(TypedDict):
    """Represents the metadata about a node or ontology."""

    subsets: list
    xrefs: list
    basicPropertyValues: list[Property]


class Graph(TypedDict):
    """A graph corresponds to an ontology."""

    id: str
    meta: Meta
    nodes: list
    edges: list[Edge]
    equivalentNodesSets: Any
    logicalDefinitionAxioms: Any
    domainRangeAxioms: Any
    propertyChainAxioms: Any


class Graphs(TypedDict):
    """Represents a list of OBO graphs."""

    graphs: list[Graph]
