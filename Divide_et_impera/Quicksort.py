import random
import time

def swap(A : list[int], i : int, j : int):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def pivot(A : list[int], start : int, end : int) -> int:
    perno = A[start]
    j = start
    for i in range(start +1, end):
        if A[i] < perno:
            j += 1
            swap(A, i, j)
    A[start] = A[j]
    A[j] = perno
    return j


def quicksort(A : list[int], start : int, end : int):
    if start < end -1:
        j = pivot(A, start, end)
        quicksort(A, start, j)
        quicksort(A, j+1 ,end)


def main():
    print("=" * 50)
    print("          QUICKSORT TESTING")
    print("=" * 50)

    n = 10   # grandezza array (modifica se vuoi)

    print(f"\nDimensione array: {n}\n")

    # -------------------------------
    # CASO MEDIO: array random
    # -------------------------------
    A = [random.randint(0, 100) for _ in range(n)]
    B = A.copy()

    print("Caso medio: array random (O(n log n))...")
    print("Array : ", A)

    start = time.time()
    quicksort(A, 0, len(A))
    end = time.time()
    print("Array  ordinato: ", A)
    

    print(f"Tempo: {end - start:.6f} secondi")

    # -------------------------------
    # CASO PEGGIORE: array ORDINATO
    # -------------------------------
    print("\nCaso peggiore: array ordinato crescente (O(n^2))...")

    B.sort()  # ordino per produrre il caso pessimo
    print("Array : ", B)

    start = time.time()
    quicksort(B, 0, len(B))
    end = time.time()

    print("Array ordinato : ", B)
    print(f"Tempo: {end - start:.6f} secondi")

    print("\n=== COMPLESSITÀ ===")
    print(" • Caso medio:    O(n log n)")
    print(" • Caso pessimo:  O(n²)")
    print(" • Caso migliore: O(n log n) (pivot perfettamente centrale)")
    print("=" * 50)


if __name__ == "__main__":
    main()