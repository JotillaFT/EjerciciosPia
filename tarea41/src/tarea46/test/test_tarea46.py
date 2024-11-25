from main.tarea46 import   listaPares

def test_funcion():
    assert listaPares([2,4,6]) == True
    assert listaPares([2,4,5,6,9,44]) == False
