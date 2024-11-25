if __name__=="__main__":
    divisas = {"Euro":"€","Dollar":"$","Yen":"¥"}
    simbolo = input("Indica la divisa que quieres saber su simbolo\n")
    simbolo = simbolo.title()
    if simbolo in divisas:
        print(divisas[simbolo])
    else:
        print("Esa divisa no esta en el diccionario")   