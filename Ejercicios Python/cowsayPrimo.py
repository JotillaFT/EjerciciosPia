import cowsay
if __name__=="__main__":
    n=input("Introduce un numero entero positivo\n")
    n = int(n)
    primo = True
    division=0
    for a in range(1,n):
        if n%a == 0:
            division+=1
        if division>1:
            primo=False                
    if primo:
        cowsay.cow(f"El numero {n} primo")
    else:
        print(f"El numero {n} no es primo")