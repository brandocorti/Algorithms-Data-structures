from typing import Optional
import math


class Node:  # Nodo di un Albero binario
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinaryTree:
    def __init__(self, root_key: int):
        self.root = Node(root_key)

    def insertLeft(self, parent: Node, key: int):
        new_node = Node(key)
        if parent.left is None:
            parent.left = new_node
        else:
            new_node.left = parent.left
            parent.left = new_node

    def insertRight(self, parent: Node, key: int):
        new_node = Node(key)
        if parent.right is None:
            parent.right = new_node
        else:
            new_node.right = parent.right
            parent.right = new_node

    def DeleteLeft(self, parent: Node):
        if parent.left is not None:
            parent.left = None
        else:
            print("Nessun figlio sinistro da eliminare")

    def DeleteRight(self, parent: Node):
        if parent.right is not None:
            parent.right = None
        else:
            print("Nessun figlio destro da eliminare")

    def print_tree(self, node: Optional[Node], level: int = 0, side: str = "root"):
        if node is not None:
            indent = "  " * level
            print(f"{indent}{side} -> {node.key}")
            self.print_tree(node.left, level + 1, "left")
            self.print_tree(node.right, level + 1, "right")



def main():
    print("=" * 40)
    print("  BINARY TREE TESTING ")
    print("=" * 40)

    # crea albero con radice
    tree = BinaryTree(10)
    print("Radice creata: 10\n")

    # Inserimenti automatici
    print("➡️ Inserimenti iniziali...")
    tree.insertLeft(tree.root, 5)
    tree.insertRight(tree.root, 7)
    tree.insertLeft(tree.root.left, 2) #type: ignore
    tree.insertRight(tree.root.right, 9) #type: ignore
    print("\n✅ Albero dopo gli inserimenti:")
    tree.print_tree(tree.root)

    # Eliminazioni di test
    print("\n🪓 Rimozione del sottoalbero sinistro di 5...")
    tree.DeleteLeft(tree.root.left) #type: ignore
    print("\n✅ Albero dopo deleteLeft(5):")
    tree.print_tree(tree.root)

    print("\n🪓 Rimozione del sottoalbero destro di 7...")
    tree.DeleteRight(tree.root.right) #type: ignore

    print("\n✅ Albero dopo deleteRight(7):")
    tree.print_tree(tree.root)

    # Interazione da terminale
    print("\n--- Modalità interattiva ---")
    print("Comandi disponibili:")
    print("  [1] Inserisci a sinistra della radice")
    print("  [2] Inserisci a destra della radice")
    print("  [3] Elimina sottoalbero sinistro")
    print("  [4] Elimina sottoalbero destro")
    print("  [5] Stampa albero")
    print("  [0] Esci")

    while True:
        try:
            choice = int(input("\nScegli un'operazione: "))
        except ValueError:
            print("Inserisci un numero valido.")
            continue

        if choice == 0:
            print("\n Fine del test.")
            break

        elif choice == 1:
            val = int(input("Valore da inserire a sinistra: "))
            tree.insertLeft(tree.root, val)
            print("✅ Nodo inserito a sinistra della radice.")
            tree.print_tree(tree.root)

        elif choice == 2:
            val = int(input("Valore da inserire a destra: "))
            tree.insertRight(tree.root, val)
            print("✅ Nodo inserito a destra della radice.")
            tree.print_tree(tree.root)

        elif choice == 3:
            tree.DeleteLeft(tree.root)
            print("✅ Sottoalbero sinistro eliminato.")
            tree.print_tree(tree.root)

        elif choice == 4:
            tree.DeleteRight(tree.root)
            print("✅ Sottoalbero destro eliminato.")
            tree.print_tree(tree.root)

        elif choice == 5:
            tree.print_tree(tree.root)

        else:
            print("Comando non valido.")


# Esegui il main
if __name__ == "__main__":
    main()
