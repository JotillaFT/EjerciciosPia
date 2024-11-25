if __name__ == "__main__":
    numeros=[]
    for a in range(5):
        num = input(f"Introduce el {a+1}º numero ganador de la loteria: \n")
        numeros.append(num)
    numeros.sort()
    for a in numeros:
        print(f"Los numeros de la loteria son: {a}\n")