def funcionLista(lista,funcion):
    if lista or funcion:
        nuevaLista=[funcion(elemento) for elemento in lista]
        return nuevaLista
    else:
        raise(TypeError("Faltan argumentos"))

def pasarFuncion(n):
    if n>0:
        return n*3
    else:
        raise(ValueError("Solo numeros positivos"))

if __name__=="__main__":
    lista = list(range(20))
    nuevaLista = funcionLista(lista,pasarFuncion)
    print(lista)
    print(nuevaLista)