if __name__=="__main__":
    n1=input("Introduce el numero a dividir\n")
    n1=int(n1)
    n2=input("Introduce el numero que va a dividir\n")
    n2=int(n2)
    if n2==0:
        print("ERROR ERORR NO SE PUEDE DIVIDIR ENTRE 0")
    else:
        n3=n1/n2
        print(f"El resultado de la division de {n1} entre {n2} es {n3}")