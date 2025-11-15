from binary_tree import Node, BinaryTree
from typing import Optional


# Funzione per la ricerca di un nodo: ritorna (nodo, padre)
def lookup(t: Optional[Node], x: int):
    parent: Optional[Node] = None
    u = t
    while u is not None and u.key != x:
        parent = u
        if x < u.key:
            u = u.left
        else:
            u = u.right
    return u, parent


# Funzione per collegare un figlio a un padre
def link(p: Optional[Node], u: Optional[Node], x: int):
    if p is None:
        return
    if x < p.key:
        p.left = u
    else:
        p.right = u


# Inserimento BST
def insertNode(t: Optional[Node], x: int, v: int) -> Node:
    p: Optional[Node] = None
    u: Optional[Node] = t

    while u is not None and u.key != x:
        p = u
        if x < u.key:
            u = u.left
        else:
            u = u.right

    # Caso: già presente → aggiorno
    if u is not None:
        u.key = v
        return t #type: ignore

    # Caso: nuovo nodo
    n = Node(x)

    if p is None:  # albero vuoto
        return n

    link(p, n, x)
    return t #type: ignore


# Eliminazione BST
def removeNode(t: Optional[Node], x: int) -> Optional[Node]:
    u, p = lookup(t, x)

    if u is None:
        return t

    # Caso: 2 figli → successore
    if u.left is not None and u.right is not None:
        s_parent = u
        s = u.right
        while s.left is not None:
            s_parent = s
            s = s.left

        u.key = s.key
        u = s
        p = s_parent
        x = u.key

    # Caso: 0 o 1 figlio
    if u.left is not None:
        T = u.left
    else:
        T = u.right

    if p is None:  # era la radice
        return T

    link(p, T, x)
    return t


# Minimo
def min_Node(T: Node):
    while T.left is not None:
        T = T.left
    return T


# Massimo
def max_Node(T: Node):
    while T.right is not None:
        T = T.right
    return T

def main():
    print("=" * 40)
    print("      BINARY SEARCH TREE TESTING      ")
    print("=" * 40)

    # Creazione albero
    print("\nCreazione albero con insertNode...")
    t: Optional[Node] = None

    values = [17, 7, 33, 1, 8, 21, 40, 5, 9]
    for v in values:
        t = insertNode(t, v, v)

    print("\n🌳 Albero iniziale:")
    tree = BinaryTree(0)  
    tree.root = t #type: ignore
    tree.print_tree(t)


    # Test lookup
    print("\n🔍 Test lookup(8):")
    node, parent = lookup(t, 8)
    print("Nodo trovato:", node.key if node else None)
    print("Padre:", parent.key if parent else None)

    # Eliminazioni
    print("\n🪓 Rimozione nodo foglia (9):")
    t = removeNode(t, 9)
    tree.root = t #type: ignore
    tree.print_tree(t)

    print("\n🪓 Rimozione nodo con 1 figlio (7):")
    t = removeNode(t, 7)
    tree.root = t #type: ignore
    tree.print_tree(t)

    print("\n🪓 Rimozione nodo con 2 figli (33):")
    t = removeNode(t, 33)
    tree.root = t #type: ignore
    tree.print_tree(t)

    print("\n🌲 BST finale:")
    tree.print_tree(t)



if __name__ == "__main__":
    main()
