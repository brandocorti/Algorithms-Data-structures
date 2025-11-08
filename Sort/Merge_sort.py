import time 
import random
import math

start = time.time()

def merge(array : list[int], first : int, last : int, middle : int): #  merge fonde le 2 metà ordinate, costo O(n)
    supp_array = [0] * len(array)   # vettore di appoggio

    i = first                       # scandisce A[primo...mezzo]
    j = middle + 1                  # scandisce A[mezzo+1...ultimo]
    k = first                       # scandisce B[primo...ultimo]

    # finche una delle due metà A[first...middle] e A[middle+1...last] è esaurita
    # confronto tra indice i e j, il minore viene copiato in B
    while i <= middle and j <= last:    
        if array[i] <= array[j]:        
            supp_array[k] = array[i]
            i += 1
        else:
            supp_array[k] = array[j]
            j += 1
        k += 1

    # Copio eventuali elementi rimasti nella prima metà
    while i <= middle:
        supp_array[k] = array[i]
        i += 1
        k += 1

    #copio eventuali elementi rimasti nella seconda meta
    while j <= last:
        supp_array[k] = array[j]
        j += 1
        k += 1

    #ricopia i valori ordinate nel vettore OG
    for h in range(first, last+ 1):
        array[h] = supp_array[h]
        


def merge_sort(array : list[int], first : int, last : int):
    if first < last:
        middle = math.floor((first + last)/2)
        merge_sort(array, first, middle)
        merge_sort(array, middle + 1, last)
        merge(array, first, last, middle)

        

def main():
    print("=" * 40)
    print("MERGE SORT DEMO ")
    print("=" * 40)

    dim = 10
    array = [random.randint(0, 9) for _ in range(dim)]
    
    print("Unsorted Array: ", array)
    
    
    first = 0
    last = dim -1

    merge_sort(array, first, last)

    end = time.time()

    print("Sorted array: ", array)
    print("=" * 40)
    print(f"Dimension of Array: {dim}")
    print(f"Complessità teorica: O(n log n)") # nel caso peggiore
    print(f"Caso Ottimo = caso Medio = caso Pessimo")
    print("=" * 40)
    print(f"\nEsecution time : {(end - start):.6f} secondi")

if __name__ == "__main__":
    main()
