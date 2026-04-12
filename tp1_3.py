
from collections.abc import Sequence

def main(cajas: Sequence[tuple[float, float, float]]) -> tuple[float, list[tuple[int, tuple[float, float]]]]:
    # solucion por programacion dinamica
    # pila_mas_alta[1] = mejor_caja_no_apilada
    # pila_mas_alta[n] = pila_mas_alta[n-1] + mejor_caja_no_apilada

    n = len(cajas)

    orientaciones = []
    for i, (x, y, z) in enumerate(cajas):
        orientaciones.append((i, x, z, y))  # base (x,z), altura y

    orientaciones.sort(key=lambda c: (c[1] * c[2]), reverse=True)

    dp = [0] * n
    parent = [-1] * n

    for i in range(n):
        dp[i] = orientaciones[i][3]

    for i in range(n):
        idx_i, bx_i, by_i, h_i = orientaciones[i]

        for j in range(i):
            idx_j, bx_j, by_j, h_j = orientaciones[j]

            if bx_i < bx_j and by_i < by_j:
                if dp[j] + h_i > dp[i]:
                    dp[i] = dp[j] + h_i
                    parent[i] = j

    max_index = max(range(n), key=lambda i: dp[i])
    max_height = dp[max_index]

    torre = []
    i = max_index

    while i != -1:
        idx, bx, by, h = orientaciones[i]
        torre.append((idx, (bx, by)))
        i = parent[i]

    torre.reverse()

    return max_height, torre
