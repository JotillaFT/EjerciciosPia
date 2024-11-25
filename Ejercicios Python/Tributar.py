if __name__=="__main__":
    edad=input("Introduce tu edad\n")
    edad=int(edad)
    salario=input("Indica tu salario\n")
    salario = int(salario)
    if (edad > 16) & (salario >= 1000):
        print("Debes tributar lo siento")
    else:
        print("No debes tributar felicidades")