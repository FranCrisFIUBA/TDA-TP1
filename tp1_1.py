
def main(turnos: list[tuple[int, int]]) -> tuple[list[int], int]:
    hora_maxima = 24
    indice_tarea_por_hora: list[int] = [-1] * hora_maxima

    indice_turnos = [(i, turno) for i, turno in enumerate(turnos)]
    indice_turnos.sort(key=lambda x: x[1][1], reverse=True)

    ganancia_total = 0
    for indice, (hora_limite, ganancia) in indice_turnos:
        hora = hora_limite - 1
        while hora >= 0:
            if indice_tarea_por_hora[hora] == -1:
                indice_tarea_por_hora[hora] = indice
                ganancia_total += ganancia
                break

            hora -= 1

    orden: list[int] = []
    for i in indice_tarea_por_hora:
        if i != -1:
            orden.append(i)

    return orden, ganancia_total
