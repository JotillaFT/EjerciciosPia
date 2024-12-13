from main.tarea48 import ganador

tablero = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
tablero2 = [["X", "", ""], ["", "X", ""], ["", "", "X"]]
tablero3 = [["X", "O", "O"], ["", "X", ""], ["", "X", "O"]]


def test_ganador():
    assert ganador(tablero) == True
    assert ganador(tablero2) == True
    assert ganador(tablero3) == False
