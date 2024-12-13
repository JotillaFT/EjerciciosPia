from main.tarea42 import calcCilin, calcCircun
import pytest

def test_circun():
    assert calcCircun(2) == 12.56
    assert calcCircun(4) == 50.24
    
def test_cilin():
    assert calcCilin(2,2) == 25.12
    assert calcCilin(4,2) == 100.48
    
def test_error():
    with pytest.raises(ValueError):
        calcCircun(-1)
    with pytest.raises(ValueError):
        calcCilin(-1,-5)
    with pytest.raises(ValueError):
        calcCilin(-2,5)
    with pytest.raises(ValueError):
        calcCilin(2,-5)