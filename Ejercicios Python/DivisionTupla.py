def division (n,m):
    c = n/m
    r = n%m
    return (c,r)
if __name__ == "__main__":
    comprobante = True
    while comprobante:
        try:
            tupla = ()
            n = input("Introduce el dividendo\n")
            n = float(n)
            m = input("Introduce el divisor\n")
            m = float(m)          
            tupla = division(n,m)
            print(f"En la division entre {n} y {m} el cociente es {tupla[0]} y el resto {tupla[1]}")              
        except ValueError:
            print("Escribe un numero")