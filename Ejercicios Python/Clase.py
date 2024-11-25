if __name__=="__main__":
    nome=input("Indica tu nombre\n")
    nome=nome.upper()
    sexo=input("Indica tu genero H/M\n")
    sexo=sexo.upper()
    if(((nome[0]<='M') and (sexo=='M'))or((nome[0]>='N')and(sexo=='H'))):
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

    