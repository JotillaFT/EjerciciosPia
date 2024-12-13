def calcCircun (r):
    if r > 0:
        pi = 3.14
        area = pi*r**2
        return area
    else:
        raise(ValueError("Só se poden operar positivos"))
def calcCilin (r,h):
    if h > 0:
        volumen = calcCircun(r)*h
        return volumen
    else:
        raise(ValueError("Só se poden operar positivos"))
        
if __name__=="__main__":
    comprobante = True
    while comprobante:
        try:
            calc = input("Quieres calcular una circunferencia o un cilindro?\n")
            calc = calc.lower()
            if calc == "circunferencia":
                while comprobante:
                    r = input("Introduce el radio\n")
                    r = float(r)
                    if r>0:
                        area = calcCircun(r)
                        print(f"El area de tu circunferencia es: {area}")
                        comprobante = False
                    else:
                        print("Escribe un numero positivo")              
            elif calc == "cilindro":
                while comprobante:
                    r = input("Introduce el radio\n")
                    r = float(r)
                    h = input("Introduce la altura\n")
                    h = float(h)
                    if r>0 and h>0:
                        volumen = calcCilin(r,h)
                        print(f"El volumen de tu cilindro es: {volumen}")
                        comprobante = False
                    else:
                        print("Escribe numeros positivos")
            else:
                print("Introduce una opción correcta")
        except ValueError:
            print("Escribe un numero")