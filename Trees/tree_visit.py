from binary_tree import BinaryTree, Node


# --- VISITE IN PROFONDITÀ ---

def preorder(node: Node):
    """Visita PREORDER: nodo → sinistra → destra"""
    if node is not None:
        print(node.key, end=" ")
        preorder(node.left)    # type: ignore
        preorder(node.right)   # type: ignore


def inorder(node: Node):
    """Visita INORDER: sinistra → nodo → destra"""
    if node is not None:
        inorder(node.left)     # type: ignore
        print(node.key, end=" ")
        inorder(node.right)    # type: ignore


def postorder(node: Node):
    """Visita POSTORDER: sinistra → destra → nodo"""
    if node is not None:
        postorder(node.left)   # type: ignore
        postorder(node.right)  # type: ignore
        print(node.key, end=" ")


# --- MAIN ---

def main():
    print("=" * 45)
    print("🌳  TREE VISIT DEMO (DFS)  🌳".center(45))
    print("=" * 45)

    # Costruzione dell’albero di esempio
    tree = BinaryTree(17)
    tree.insertLeft(tree.root, 7)
    tree.insertRight(tree.root, 33)
    tree.insertLeft(tree.root.left, 1)     # type: ignore
    tree.insertRight(tree.root.left, 8)    # type: ignore
    tree.insertLeft(tree.root.right, 21)   # type: ignore
    tree.insertRight(tree.root.right, 40)  # type: ignore

    print("\n🌲 Struttura dell’albero:")
    tree.print_tree(tree.root)

    print("\n🔎 Visite in profondità:")

    print("\n➡️ PREORDER:")
    preorder(tree.root)
    print()

    print("\n➡️ INORDER:")
    inorder(tree.root)
    print()

    print("\n➡️ POSTORDER:")
    postorder(tree.root)
    print()

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()




    


