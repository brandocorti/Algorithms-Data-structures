class MinPriorityQueue:
    """
    Implementazione di una Min Priority Queue
    tramite Binary Min Heap.

    Proprietà mantenuta:
        parent <= children

    Complessità:
        insert()       -> O(log n)
        extract_min()  -> O(log n)
        peek()         -> O(1)
        build_heap()   -> O(n)
    """

    def __init__(self):
        self.heap = []


    def _parent(self, i: int) -> int: #Padre O(1)
        return (i - 1) // 2


    def _left(self, i: int) -> int: #figlio sx O(1)
        return (2 * i) + 1


    def _right(self, i: int) -> int: #figlio destro O(1)
        return (2 * i) + 2


    def _swap(self, i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


    def _min_heap_restore(self, i: int, dim: int) -> None:
        """
        Ripristina la proprietà di Min Heap verso il basso.

        Utilizzato dopo extract_min().

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n) per ricorsione
        """

        min_index = i

        left = self._left(i)
        right = self._right(i)

        if left < dim and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < dim and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self._swap(i, min_index)
            self._min_heap_restore(min_index, dim)



    def _max_heap_restore(self, i: int, dim: int) -> None:
        """
        Ripristina la proprietà di Max Heap.

        Non utilizzato nella Min Priority Queue,
        mantenuto solo come riferimento.

        Time Complexity:
            O(log n)
        """

        max_index = i

        left = self._left(i)
        right = self._right(i)

        if left < dim and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < dim and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self._swap(i, max_index)
            self._max_heap_restore(max_index, dim)



    def _heapify_up(self, i: int) -> None:
        """
        Ripristina la proprietà di Min Heap verso l'alto.

        Utilizzato dopo insert().

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n) per ricorsione
        """

        while i > 0:

            parent = self._parent(i)

            if self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
                i = parent

            else:
                break



    def insert(self, key: int) -> None:
        """
        Inserisce un nuovo elemento.

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
        Restituisce il minimo senza rimuoverlo.

        Time Complexity:
            O(1)
        """

        if len(self.heap) == 0:
            raise IndexError("Priority Queue vuota")

        return self.heap[0]



    def extract_min(self) -> int:
        """
        Rimuove e restituisce il minimo.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(1)
        """

        if len(self.heap) == 0:
            raise IndexError("Priority Queue vuota")
        min_value = self.heap[0]

        # porto l'ultimo elemento alla radice
        self._swap(0, len(self.heap)-1)

        # elimino l'ultimo elemento
        self.heap.pop()

        # ripristino il Min Heap
        if len(self.heap) > 0:
            self._min_heap_restore(0, len(self.heap))

        return min_value



    def build_heap(self, array: list[int]) -> None:
        """
        Costruisce un Min Heap da un array.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """

        self.heap = array

        start = (len(self.heap)//2)-1

        for i in range(start, -1, -1):
            self._min_heap_restore(i, len(self.heap))


    def __str__(self) -> str:
        """
        Rappresentazione dell'heap.

        Time Complexity:
            O(n)
        """
        return str(self.heap)



def test_min_priority_queue():

    pq = MinPriorityQueue()


    print("=== INSERT ===")

    values = [8, 3, 10, 1, 6, 2]

    for value in values:
        pq.insert(value)
        print(pq)



    print("\n=== PEEK ===")
    print("Min:", pq.peek())



    print("\n=== EXTRACT MIN ===")

    while len(pq.heap) > 0:
        print("Estratto:", pq.extract_min())
        print("Heap:", pq)



    print("\n=== BUILD HEAP ===")

    array = [9, 4, 7, 1, 0, 3]

    pq.build_heap(array)

    print("Heap costruito:")
    print(pq)



if __name__ == "__main__":
    test_min_priority_queue()