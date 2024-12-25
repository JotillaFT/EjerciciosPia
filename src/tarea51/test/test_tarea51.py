import pytest
from main.tarea51 import Vehiculo
coche = Vehiculo(45,900000)
def test_error():
    with pytest.raises(ValueError):
        coche.kms=60000
        coche.velMax=-78