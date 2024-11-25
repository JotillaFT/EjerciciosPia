def calcIve(coste,ive=21):
    nCoste=int(coste*(1+(ive/100)))
    return nCoste
if __name__=="__main__":
    comprobante = True
    while comprobante:
        try:
            coste=int(input("Introduce el precio del producto\n"))
            ive=input("Introduce el IVE del producto (en caso de que no, presiona Enter)\n")
            if ive:
                ive = int(ive)
                nCoste=calcIve(coste,ive)
                print(f"El nuevo coste de tu prodcuto es {nCoste}")
            else:
                nCoste=calcIve(coste)
                print(f"El nuevo coste de tu prodcuto es {nCoste}")
            comprobante = False
        except ValueError:
            print("Introduce un numero porfa")