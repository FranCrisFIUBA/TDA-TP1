
from collections.abc import Sequence

# algoritmo propuesto:
# OPT(0) = 0
# OPT(1) = altura de la primer caja
# OPT(i) = altura maxima de una torre cuya caja superior es i
# OPT(i+1) = si la caja i+1 puede apilarse OPT(i) + altura de la caja i+1

# OPT(0) = 0
# OPT(1) = y_1
# OPT(i) = altura máxima de una pila cuya caja superior es i
# OPT(i) = y_i + max( OPT(j) tal que x_j < x_i y z_j < z_i )
def main(cajas: Sequence[tuple[float, float, float]]) -> tuple[float, list[tuple[int, tuple[float, float]]]]:

    print(cajas)

    # guardamos índices originales
    indices_cajas = [(indice, caja) for indice, caja in enumerate(cajas)]

    # ordenar por base
    indices_cajas.sort(key=lambda indice_caja: (indice_caja[1][0], indice_caja[1][2]))  # (x, z)

    n = len(indices_cajas)

    dp = [0.0] * n
    indice_caja_superior_anterior = [-1] * n

    for i in range(n):
        _, (x_i, y_i, z_i) = indices_cajas[i]
        dp[i] = y_i

    for i in range(n):
        indice_i, (x_i, y_i, z_i) = indices_cajas[i]

        for j in range(i):
            indice_j, (x_j, y_j, z_j) = indices_cajas[j]

            if x_j < x_i and z_j < z_i:
                if dp[j] + y_i > dp[i]:
                    dp[i] = dp[j] + y_i
                    indice_caja_superior_anterior[i] = j

    # índice de la mejor torre
    mejor_caso = max(range(n), key=lambda i: dp[i])
    altura_maxima = dp[mejor_caso]

    # reconstruccion
    pila = []
    i = mejor_caso
    while i != -1:
        indice, (x, y, z) = indices_cajas[i]
        pila.append((indice, (x, z)))
        i = indice_caja_superior_anterior[i]

    return altura_maxima, pila
