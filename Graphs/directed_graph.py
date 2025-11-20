from graph_node import GraphNode
from graph_edge import Edge

class DirectedGraph:
    def __init__(self):
        self.nodes : dict[int, GraphNode] = {}

    def add_node(self, key : int) -> GraphNode:
        if key not in self.nodes:
            self.nodes[key] = GraphNode(key)
        return self.nodes[key]
    
    def add_edge(self, a: int, b : int):
        na = self.add_node(a)
        nb = self.add_node(b)
        na.neighbors.append(Edge(nb))


    def size(self) -> int:
        return len(self.nodes)
    
    def delete_edge(self, a : int, b : int):
        if a not in self.nodes:
            return
        node_a = self.nodes[a]

        #tiene solo gli archi che non puntano a b
        node_a.neighbors = [
            edge for edge in node_a.neighbors if edge.to.key != b
        ]

    def delete_node(self, key : int):
        # se il nodo non esiste niente da fare
        if key not in self.nodes:
            return
        
        #elimna il nodo dalla lista dei nodi
        del self.nodes[key]

        # rimuove tutti gli archi entranti veerso questo nodo
        for node in self.nodes.values():
            node.neighbors = [
                edge for edge in node.neighbors if edge.to.key != key
            ]
    

    def print_graph(self):
        print("\nGRAFO:")
        for key, node in self.nodes.items():
            neigh = [edge.to.key for edge in node.neighbors]
            print(f"{key} -> {neigh}")
        print()




def main():
    print("=" * 40)
    print("        GRAPH STRUCTURE TEST")
    print("=" * 40)

    g = DirectedGraph()

    # Aggiunta nodi e archi
    print("\n➡️   Creo un grafo:")
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    g.print_graph()

    # Test size
    print(f"📦 Numero di nodi: {g.size()}")

    # Test delete_edge
    print("\n🪓 Elimino edge 1 → 3")
    g.delete_edge(1, 3)
    g.print_graph()

    # Test delete_node
    print("\n🪓 Elimino nodo 4 (e tutti gli archi che puntano a 4)")
    g.delete_node(4)
    g.print_graph()

    print(f"📦 Numero di nodi dopo delete: {g.size()}")

    print("\n=== TEST COMPLETATO ===")


if __name__ == "__main__":
    main()
