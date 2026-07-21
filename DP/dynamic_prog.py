"""
Dynamic Programming Algorithms

Questo file contiene alcune implementazioni classiche
di problemi risolti tramite programmazione dinamica.

La programmazione dinamica consiste nel:
- dividere il problema in sottoproblemi più piccoli
- memorizzare le soluzioni già calcolate
- evitare di ricalcolare gli stessi casi

"""

# ============================================================
# HATEVILLE 
# ============================================================

"""
Definizione del problema:

Dato un insieme di case disposte in linea,
ogni casa contiene un valore D[i].

Un ladro vuole massimizzare il valore rubato,
ma non può rubare da due case consecutive.

Esempio:

D = [5, 10, 3, 20]

Soluzione:
prendo 10 + 20 = 30

Ricorrenza:

DP[i] = max(
            DP[i-1],
            DP[i-2] + D[i]
          )

dove:
- DP[i-1] -> salto la casa corrente
- DP[i-2]+D[i] -> prendo la casa corrente


Complessità:
    Tempo: O(n)
    Spazio: O(n)

"""

def Hateville_iter(D: list[int], n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return D[0]

    DP = [0] * n

    DP[0] = D[0]
    DP[1] = max(D[0], D[1])

    for i in range(2, n):
        DP[i] = max(
            DP[i-1],
            DP[i-2] + D[i]
        )

    return DP[n-1]




# ============================================================
# KNAPSACK 0/1
# ============================================================

"""
Definizione del problema:

Dato:

- n oggetti
- peso w[i]
- profitto p[i]
- capacità massima C

Bisogna scegliere gli oggetti da inserire
nello zaino massimizzando il profitto,
senza superare la capacità.

Ogni oggetto può essere preso al massimo una volta.


Stato DP:

DP[i][c]

rappresenta:

massimo profitto usando i primi i oggetti
con capacità massima c.


Ricorrenza:

Se il peso dell'oggetto è maggiore
della capacità:

DP[i][c] = DP[i-1][c]


Altrimenti:

DP[i][c] =
max(
    DP[i-1][c],
    DP[i-1][c-w[i]] + p[i]
)

Complessità:
Tempo:
    O(n*C)
Spazio:
    O(n*C)

"""


def knapsack(w: list[int], p: list[int], n: int, C: int) -> int:

    DP = [
        [0 for c in range(C+1)]
        for i in range(n+1)
    ]

    for i in range(1, n+1):
        for c in range(1, C+1):

            if w[i-1] <= c:

                DP[i][c] = max(
                    DP[i-1][c],
                    DP[i-1][c-w[i-1]] + p[i-1]
                )

            else:
                DP[i][c] = DP[i-1][c]

    return DP[n][C]


# ============================================================
# LONGEST COMMON SUBSEQUENCE
# ============================================================

"""
Definizione del problema:

Date due sequenze T e U,
trovare la più lunga sottosequenza
presente in entrambe.

Una sottosequenza mantiene l'ordine degli elementi
ma non necessariamente sono consecutivi.


Esempio:

T = ABCBDAB
U = BDCABA

LCS possibile:

BCBA


Stato:

DP[i][j]

lunghezza della LCS tra:
- primi i caratteri di T
- primi j caratteri di U


Ricorrenza:

Se T[i-1] == U[j-1]:

DP[i][j] = DP[i-1][j-1] + 1


Altrimenti:

DP[i][j] =
max(
    DP[i-1][j],
    DP[i][j-1]
)


Complessità:
Tempo:
    O(n*m)
Spazio:
    O(n*m)

"""

def LCS(T: list[str], U: list[str], n: int, m: int) -> int:

    DP = [
        [0 for j in range(m+1)]
        for i in range(n+1)
    ]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if T[i-1] == U[j-1]:

                DP[i][j] = DP[i-1][j-1] + 1

            else:
                DP[i][j] = max(
                    DP[i-1][j],
                    DP[i][j-1]
                )


    return DP[n][m]

def main():


    print("======== HATEVILLE ========")

    houses = [5,10,3,20,7]

    result = Hateville_iter(
        houses,
        len(houses)
    )

    print("Case:", houses)
    print("Maximum money:", result)



    print("\n======== KNAPSACK ========")

    weights = [2,3,4,5]
    profits = [3,4,5,8]

    capacity = 5


    result = knapsack(
        weights,
        profits,
        len(weights),
        capacity
    )


    print("Weights:", weights)
    print("Profits:", profits)
    print("Capacity:", capacity)
    print("Maximum profit:", result)



    print("\n======== LCS ========")


    T = list("ABCBDAB")
    U = list("BDCABA")


    result = LCS(
        T,
        U,
        len(T),
        len(U)
    )


    print("String 1:", "".join(T))
    print("String 2:", "".join(U))
    print("LCS length:", result)


if __name__ == "__main__":
    main()