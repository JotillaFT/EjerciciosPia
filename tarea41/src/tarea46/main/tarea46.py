def listaPares(lista):
    pares = (n % 2 == 0 for n in lista)
    if all(pares):
        return True
    else:
        return False
    
if __name__ == "__main__":
    lista = [2,4,6,7,8]
    if listaPares(lista):
        print("Todos los numeros son pares")
    else:
        print("Alguno de los numeros es impar")