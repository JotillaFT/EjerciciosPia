from main.tarea45 import esPrimo, listaPrimos
import pytest

def test_primos():
    assert esPrimo(5) == 5
    assert listaPrimos(listaN(),esNPrimo) == [1, 2, 3, 5, 7, 11, 13, 17, 19]

def test_errores():
    with pytest.raises(ValueError):
        esPrimo(-8)    
    with pytest.raises(TypeError):
        listaPrimos(listaN())
    with pytest.raises(TypeError):
        listaPrimos()

def listaN():
    return list(range(20))

def esNPrimo(num):
    primo = True
    if num >= 0:
        for n in range(2,num):
            if num % n == 0:
                primo = False
        if primo:
            return num