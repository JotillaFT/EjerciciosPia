def sumN (n):
    if n>0:
        a = n*(n+1)/2
        return a
    else:
         raise(ValueError("Só se poden sumar positivos"))
if __name__=="__main__":
    comprobante = True
    while comprobante: 
        try:       
            n = input("Introduce un numero entero positivo\n")
            n= int(n)
            if n <= 0:
                print("Numero positivo por favor")
            else:
                print(sumN(n))
                comprobante=False
        except ValueError:
            print("Te dije un numero entero")