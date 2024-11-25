if __name__=="__main__":
    edad=input("Cuantos años tienes\n")
    edad = int(edad)
    for a in range(edad):
        print(f"Cumpliste {a} años hace {edad-a} años")