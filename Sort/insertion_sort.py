import random
import time

start = time.time()

def main():
    print("=" * 40)
    print("INSERTION SORT DEMO ")
    print("=" * 40)

    dim = 10
    array = [random.randint(0, 9) for _ in range(dim)] # caso Pessimo

    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9] # caso Ottimo

    print("Unsorted Array: ", array)

    for i in range(1, dim):
        temp = array[i]
        j = i
        while j > 0 and array[j-1] > temp: # sposta a destra gli elementi maggiori 
            array[j] = array[j-1]
            j -= 1
        array[j] = temp             # mette temp nella posizione ideale

    end = time.time()

    print("Sorted array: ", array)
    print("=" * 40)
    print(f"Dimension of Array: {dim}")
    print(f"Complessità teorica: O(n²) nel caso pggiore") # nel caso peggiore
    print(f"O(n) nel caso in cui l'array è ordinato")
    print("=" * 40)
    print(f"\nEsecution time : {(end - start):.6f} secondi")

if __name__ == "__main__":
    main()