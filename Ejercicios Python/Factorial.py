def factorial(n):
    nfact=1
    for a in range(1,n+1):
        nfact*=a
    return nfact
if __name__=="__main__":
    comprobante = True
    while comprobante: 
        try:       
            n = input("Introduce un numero entero positivo\n")
            n= int(n)
            if n <= 0:
                print("Numero positivo por favor")
            else:
                print(factorial(n))
                comprobante=False
        except ValueError:
            print("Te dije un numero entero")