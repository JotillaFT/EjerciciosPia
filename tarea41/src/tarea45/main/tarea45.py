def esPrimo(num):
    primo = True
    if num >= 0:
        for n in range(2,num):
            if num % n == 0:
                primo = False
        if primo:
            return num
    else: 
        raise(ValueError("Numeros positivos por favor"))

def listaPrimos(lista,funcion):
    if lista or funcion:
        listaPrimos = list(filter(funcion,lista))   
        return listaPrimos
    else:
        raise(TypeError("Faltan argumentos"))
if __name__ == "__main__":
    lista = list(range(20))
    newLista = listaPrimos(lista,esPrimo)
    print(newLista)