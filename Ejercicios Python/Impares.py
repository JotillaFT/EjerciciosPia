if __name__=="__main__":
    num=input("Escribe un numero entero\n")
    num=int(num)
    cadena=''
    for a in range(num):
        if a%2!=0:
            b=str(a)+','
            cadena=cadena+b
    print(cadena)