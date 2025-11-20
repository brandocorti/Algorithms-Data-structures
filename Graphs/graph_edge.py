from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph_node import GraphNode

class Edge:
    def __init__(self, to: GraphNode):
        self.to = to