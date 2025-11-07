import random
import time

start = time.time()

def min_index(array : list[int], k: int, dim: int) -> int:
    minimum = k                                 # Posizione del minimo Parziale
    for h in range(k+1, dim):
        if array[h] < array[minimum]:           # Nuovo Minimo parziale
            minimum = h
    return minimum

print("Selection Sort: O(n^2)")
print("Array Dimension = 10")

def main():
    print("=" * 40)
    print(" SELECTION SORT DEMO ")
    print("=" * 40)

    dim = 10
    array = [random.randint(0, 9) for _ in range(dim)]
    print("Unsorted Array: ", array)

    swaps = 0
    for i in range(dim - 1):
        j = min_index(array, i, dim)
        if i != j:
            array[i],array[j] = array[j], array[i]
            swaps += 1

    end = time.time()

    print("Sorted array: ", array)
    print("=" * 40)
    print(f"Dimension of Array: {dim}")
    print(f"Number of swaps : {swaps}")
    print(f"Complessità teorica: O(n²)")
    print("=" * 40)
    print(f"\nEsecution time : {(end - start):.6f} secondi")

if __name__ == "__main__":
    main()
    













