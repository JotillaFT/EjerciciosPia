def calcImc(peso,altura):
    imc = peso/((altura/100)**2)
    return imc

if __name__=="__main__":
    comprobante = True
    while comprobante:
        try:
            peso=int(input("Introduce tu peso en Kg: "))
            altura = int(input("Introduce tu altura en cm: "))
            if peso<=0 or altura <=0:
                print("Numero positivo porfi")
            else:
                imc= calcImc(peso,altura)
                print(f"Tu IMC es: {imc:.2f}")
                comprobante=False
        except ValueError:
            print("Introduce un numero porfa")