if __name__=="__main__":
    print("Cuantas horas has trabajado hoy?")
    horas=input()
    horas=int(horas)
    print("Cuanto cobras por hora?")
    sueldo=input()
    sueldo=int(sueldo)
    salario=horas*sueldo
    print(f"Te corresponde cobrar {salario} por tu trabajo de hoy")