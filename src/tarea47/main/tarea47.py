def filtroInmueble(lista, precio):
    newLista = []
    for inmueble in lista:
        if compPrecio(inmueble, precio):
            inmueble["precio"] = calcPrecio(inmueble)
            newLista.append(inmueble)
    return newLista


def calcPrecio(inmueble):
    precio = 0
    metros = inmueble["metros"]
    hab = inmueble["habitacións"]
    garaje = inmueble["garaxe"]
    antiguedad = 2024 - inmueble["ano"]
    precio = (metros * 1000) + (hab * 5000)
    if garaje:
        precio = precio + 15000
    precio = precio * (1 - (antiguedad / 100))
    if inmueble["zona"] == "B":
        precio = precio * 1.5
    return precio


def compPrecio(inmueble, precio):
    inmueblePrecio = calcPrecio(inmueble)
    if inmueblePrecio <= precio:
        return True
    else:
        return False


if __name__ == "__main__":
    listaInmuebles = [
        {"ano": 2000, "metros": 100, "habitacións": 3, "garaxe": True, "zona": "A"},
        {"ano": 2012, "metros": 60, "habitacións": 2, "garaxe": True, "zona": "B"},
        {"ano": 1980, "metros": 120, "habitacións": 4, "garaxe": False, "zona": "A"},
        {"ano": 2005, "metros": 75, "habitacións": 3, "garaxe": True, "zona": "B"},
        {"ano": 2015, "metros": 90, "habitacións": 2, "garaxe": False, "zona": "A"},
    ]
    precio = int(input("Introduce el precio a comparar\n"))
    listaInmuebles2 = filtroInmueble(listaInmuebles, precio)
    print(listaInmuebles2)
