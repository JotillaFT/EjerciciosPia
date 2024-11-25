if __name__=="__main__":
    listaCompra = {}
    comprobante = True
    total = 0
    while comprobante:
        articulo = input("Indica el articulo a comprar\n")
        error = True
        while error:
            try:
                precio = int(input("Indica precio del producto\n"))
                if precio >0:
                    listaCompra[articulo]=precio
                    error = False
                else:
                    print("Indica un precio correcto, nada es gratis")
            except ValueError:
                print("Indica un precio correctamente")
        cont=input("Quiere introducir otro articulo? (S/N)?")
        if cont == "N":
            comprobante=False
    for clave in listaCompra.keys():
        total+=listaCompra[clave]
        print("{}-------------{}€".format(clave,listaCompra[clave]))
    print(f"Total-------------{total}€")     