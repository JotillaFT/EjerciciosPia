from main.tarea44 import funcionLista,pasarFuncion
import pytest

def test_funcion():
    assert funcionLista(lista(),funcion) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57]
    assert pasarFuncion(5) == 15

def test_error():
    with pytest.raises(TypeError):
        funcionLista(funcion)   
    with pytest.raises(ValueError):
        pasarFuncion(-5) 
def lista():
    return list(range(20))

def funcion(n):
    return n*3