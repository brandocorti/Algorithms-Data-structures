from __future__ import annotations
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from graph_edge import Edge

class GraphNode:
    def __init__(self, key: int):
        self.key: int = key
        self.neighbors: list[Edge] = []




