if __name__=="__main__":
    n=input("Introduce un numero entero positivo\n")
    n = int(n)
    resultado = 0
    for a in range(n+1):
        resultado+=a
    print(resultado)