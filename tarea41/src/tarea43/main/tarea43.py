def iva21(n):
    if n>0:
        return n*1.21
    else:
        raise(ValueError("Datos incorrectos"))
def iva4(n):
    if n>0:
        return n*1.04
    else:
        raise(ValueError("Datos incorrectos"))
def descuento(n):
    if n>0:
        return n*0.90
    else:
        raise(ValueError("Datos incorrectos"))
def totalCompra(lista):
    total = 0
    total_descuentos = 0
    total_iva = 0
    for index in lista:
        precio = index['precio']
        descuento = index['descuento']
        iva = index['IVA']
        if descuento:
            total += iva(descuento(precio))
            total_descuentos += precio - descuento(precio)
            total_iva += iva(descuento(precio)) - descuento(precio)
        else:
            total += iva(precio)
            total_iva += iva(precio) - precio
    return (total,total_descuentos,total_iva)

if __name__=="__main__":
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
    totales = totalCompra(listaCompra)
    print(f"El total de tu lista de la compra es: {totales[0]:.2f}\nEl total descontado de la compra es: {totales[1]:.2f}\nEl total de iva añadido de la compra es: {totales[2]:.2f}\n")   