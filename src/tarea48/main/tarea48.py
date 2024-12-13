def imprimirTablero(tablero):
    for filas in tablero:
        print(" | ".join(filas))
        print("-" * 9)


def ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False


def accion(tablero, jugador):
    fila = int(
        input(
            f"jugador {jugador} indica la fila en la que colocaras tu pieza '0','1','2'\n "
        )
    )
    columna = int(
        input(
            f"jugador {jugador} indica la columna en la que colocaras tu pieza '0','1','2'\n "
        )
    )
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
    else:
        print("Esa celda ya esta ocupada\n")
        accion(tablero, jugador)
    return tablero


def partida():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    movimientos = 0
    while True:
        imprimirTablero(tablero)
        jugador = "X"
        tablero = accion(tablero, jugador)
        movimientos += 1
        if movimientos == 9:
            break
        imprimirTablero(tablero)
        if ganador(tablero):
            break
        jugador = "O"
        tablero = accion(tablero, jugador)
        movimientos += 1
        if ganador(tablero):
            break
    if ganador(tablero):
        print(f"Enhorabuena, has ganado {jugador}")
        imprimirTablero(tablero)
    else:
        print("Habeis empatado")


if __name__ == "__main__":
    partida()
