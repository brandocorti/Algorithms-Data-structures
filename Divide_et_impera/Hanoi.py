import math

moves = 0
def hanoi(n : int, src : str, dest : str, mid : str):
    global moves

    if n == 1:  
        moves += 1                    
        print(f" mossa {moves:2d}: {src} -> {dest}")    #muovo un solo disco dalla sorgente alla dest
        
    else:
        hanoi(n -1, src, mid, dest) # sposto i primi n-1 dischi sul medio

        moves += 1
        print(f" mossa {moves:2d}: {src} -> {dest}") # sposto il disco piu grande da src a dest

        hanoi(n-1, mid, dest, src) # Sposti i n-1 dischi da mid a dest




def main():
    global moves
    moves = 0  # reset contatore

    print("=" * 55)
    print("      TORRI DI HANOI — ALGORITMO DIVIDE ET IMPERA")
    print("=" * 55)

    n = 4  # numero di dischi, puoi cambiarlo

    print(f"\nNumero di dischi: {n}\n")
    print("Il problema viene risolto ricorsivamente, dividendo in:")
    print("  • Sottoproblema 1: spostare n−1 dischi da src → aux")
    print("  • Mossa centrale: spostare il disco più grande da src → dest")
    print("  • Sottoproblema 2: spostare n−1 dischi da aux → dest\n")

    print("Sequenza delle mosse:\n")
    hanoi(n, "A", "C", "B")

    print("\nRisultati finali:")
    print(f"  ➤ Numero totale di mosse: {moves}")
    print(f"  ➤ Complessità: T(n) = 2ⁿ − 1 = {2**n - 1}")
    print(f"  ➤ Crescita esponenziale O(2ⁿ)")
    print("=" * 55)


if __name__ == "__main__":
    main()
