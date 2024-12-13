from src.tarea41.main.tarea41 import sumN
import pytest

def test_1():
    assert sumN(5) == 15
    assert sumN(10) == 55
    
def test_2():
    with pytest.raises(ValueError):
        sumN(-3)
    