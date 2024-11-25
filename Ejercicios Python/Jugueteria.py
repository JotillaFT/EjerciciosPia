def calcPeso (payasos,bonecas):
    pesoPayaso=(payasos*112)/1000
    pesoBonecas = (bonecas*75)/1000
    pesoTotal = pesoPayaso+pesoBonecas
    return pesoTotal
if __name__=="__main__":
    comprobante= True
    while comprobante:
        try:
            payasos = int(input("Cuantos payasos has vendido?\n"))
            if payasos <=0:
                print("Introduce un numero positivo")
            else:
                while comprobante:
                    try:
                        bonecas = int(input("Cuantas muñecas has vendido?\n"))
                        if bonecas <=0:
                            print("Introduce un numero positivo")
                        else:
                            peso =  calcPeso(payasos,bonecas)
                            print(f"El peso del paquete seran {peso} kg")
                            comprobante=False
                    except ValueError:
                        print("Introduce un numero porfi")
                    
        except ValueError:
            print("No has escrito un numero.")