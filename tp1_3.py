
from collections.abc import Sequence

# OPT(0) = 0
# OPT(1) = y_1
# OPT(i) = altura máxima de una pila cuya caja superior es i
# OPT(i) = y_i + max( OPT(j) tal que x_j < x_i y z_j < z_i )
def main(cajas: Sequence[tuple[float, float, float]]) -> tuple[float, list[tuple[int, tuple[float, float]]]]:
    # temporal: O(n)
    # espacial: O(n)
    indices_cajas = [(indice, caja) for indice, caja in enumerate(cajas)]

    # temporal: O(n log n)
    # espacial: O(n)
    indices_cajas.sort(key=lambda indice_caja: (indice_caja[1][0], indice_caja[1][2]))  # (x, z)

    n = len(indices_cajas)

    # temporal: O(n)
    # espacial: O(n)
    memo = [0.0] * n

    # temporal: O(n)
    # espacial: O(n)
    indice_caja_superior_anterior = [-1] * n

    # temporal: O(n)
    for i in range(n):
        _, (x_i, y_i, z_i) = indices_cajas[i]
        memo[i] = y_i

    # temporal: O(n^2)
    for i in range(n):
        indice_i, (x_i, y_i, z_i) = indices_cajas[i]

        for j in range(i):
            indice_j, (x_j, y_j, z_j) = indices_cajas[j]

            if x_j < x_i and z_j < z_i:
                if memo[j] + y_i > memo[i]:
                    memo[i] = memo[j] + y_i
                    indice_caja_superior_anterior[i] = j

    # índice de la mejor torre
    mejor_caso = max(range(n), key=lambda i: memo[i])
    altura_maxima = memo[mejor_caso]

    # reconstruccion
    pila = []
    i = mejor_caso
    while i != -1:
        indice, (x, y, z) = indices_cajas[i]
        pila.append((indice, (x, z)))
        i = indice_caja_superior_anterior[i]

    return altura_maxima, pila
