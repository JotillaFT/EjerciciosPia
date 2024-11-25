if __name__=="__main__":
    num=input("Escribe un numero positivo y entero\n")
    num=int(num)
    cadena=''
    for a in range(num+1):
        b = num-a
        b = str(b)
        cadena=cadena+b+','
    print(cadena)