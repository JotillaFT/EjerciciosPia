from main.tarea43 import iva21,iva4,descuento,totalCompra
import pytest

def test_ivas():
    assert iva21(100) == 121
    assert iva21(50) == 60.5
    assert iva4(100) == 104
    assert iva4(50) == 52
     
def test_desc():
    assert descuento(100) == 90
    assert descuento(50) == 45
    
def test_total():
    assert totalCompra(retornarLista()) == (12.229500000000002,0.5499999999999998,1.2795)
    
def test_error():
    with pytest.raises(ValueError):
        iva21(-4)
    with pytest.raises(ValueError):
        iva4(-4)
    with pytest.raises(ValueError):
        descuento(-4)
def retornarLista():
    listaCompra = [
        {
            "producto": "Pera","precio": 3.00,"descuento" : descuento,"IVA": iva21,
        },
        {
            "producto": "Manzana","precio": 5.00,"descuento" : None,"IVA": iva4,
        },
        {
            "producto": "Plátano","precio": 2.50,"descuento" : descuento,"IVA": iva21
        },
        {
            "producto": "Melocoton","precio": 1.00,"descuento" : None,"IVA": iva4
        }      
    ]
    return listaCompra
#Si quitas tods las cosas de la vida no tiene gracias, por ejemplo el queso
#Ricardo e Isaac?
#Internet y 500 Gb de almacenamiento
#Yo eso ya lo se, pero necesito que las digas tu, no yo.
#No wtf, se llama psicologia
#me alegro mucho <3
#UwU, ewe, :v,(<''<), *se sonroja*, *le abraza*