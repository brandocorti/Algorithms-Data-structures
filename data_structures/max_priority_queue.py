class MaxPriorityQueue:
    """
    Implementazione di una Max Priority Queue
    tramite Binary Max Heap.

    Proprietà mantenuta:
        parent >= children

    Complessità:
        insert()        -> O(log n)
        extract_max()   -> O(log n)
        peek()          -> O(1)
        build_heap()    -> O(n)
    """

    def __init__(self):
        """
        Inizializza una priority queue vuota.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.heap = []


    def _parent(self, i: int) -> int:
        """
        Restituisce indice del nodo padre.

        Time Complexity:
            O(1)
        """
        return (i - 1) // 2


    def _left(self, i: int) -> int:
        """
        Restituisce indice figlio sinistro.

        Time Complexity:
            O(1)
        """
        return (2 * i) + 1


    def _right(self, i: int) -> int:
        """
        Restituisce indice figlio destro.

        Time Complexity:
            O(1)
        """
        return (2 * i) + 2


    def _swap(self, i: int, j: int) -> None:
        """
        Scambia due elementi dell'heap.

        Time Complexity:
            O(1)
        """
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


    def _max_heap_restore(self, i: int, dim: int) -> None:
        """
        Ripristina la proprietà di Max Heap
        verso il basso.

        Utilizzato dopo extract_max()
        e build_heap().

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n) ricorsione
        """

        max_index = i

        left = self._left(i)
        right = self._right(i)


        if left < dim and self.heap[left] > self.heap[max_index]:
            max_index = left


        if right < dim and self.heap[right] > self.heap[max_index]:
            max_index = right


        if max_index != i:
            self._swap(i, max_index)
            self._max_heap_restore(max_index, dim)



    def _heapify_up(self, i: int) -> None:
        """
        Ripristina la proprietà Max Heap
        verso l'alto.

        Utilizzato dopo insert().

        Time Complexity:
            O(log n)

        Space Complexity:
            O(1)
        """

        while i > 0:

            parent = self._parent(i)

            if self.heap[i] > self.heap[parent]:
                self._swap(i, parent)
                i = parent

            else:
                break



    def insert(self, key: int) -> None:
        """
        Inserisce un elemento nella Max Priority Queue.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(1)
        """

        self.heap.append(key)

        index = len(self.heap) - 1

        self._heapify_up(index)



    def peek(self) -> int:
        """
        Restituisce il massimo senza rimuoverlo.

        Time Complexity:
            O(1)
        """

        if len(self.heap) == 0:
            raise IndexError("Priority Queue vuota")

        return self.heap[0]



    def extract_max(self) -> int:
        """
        Rimuove e restituisce il massimo.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(1)
        """

        if len(self.heap) == 0:
            raise IndexError("Priority Queue vuota")


        max_value = self.heap[0]


        # porta ultimo elemento alla radice
        self._swap(0, len(self.heap)-1)


        # elimina ultimo elemento
        self.heap.pop()


        # ripristina proprietà Max Heap
        if len(self.heap) > 0:
            self._max_heap_restore(0, len(self.heap))


        return max_value



    def build_heap(self, array: list[int]) -> None:
        """
        Costruisce un Max Heap da un array.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """

        self.heap = array

        start = (len(self.heap)//2)-1


        for i in range(start, -1, -1):
            self._max_heap_restore(i, len(self.heap))



    def __str__(self) -> str:
        """
        Stampa la rappresentazione dell'heap.

        Time Complexity:
            O(n)
        """
        return str(self.heap)



def test_max_priority_queue():

    pq = MaxPriorityQueue()


    print("=== INSERT ===")

    values = [8, 3, 10, 1, 6, 20, 15]

    for value in values:
        pq.insert(value)
        print(pq)



    print("\n=== PEEK ===")
    print("Massimo:", pq.peek())



    print("\n=== EXTRACT MAX ===")

    while len(pq.heap) > 0:

        print("Estratto:", pq.extract_max())
        print("Heap:", pq)



    print("\n=== BUILD HEAP ===")

    array = [4, 10, 3, 5, 1, 8]

    pq.build_heap(array)

    print("Max Heap costruito:")
    print(pq)



if __name__ == "__main__":
    test_max_priority_queue()