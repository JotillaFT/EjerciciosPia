if __name__=="__main__":
    materias = ["Matematicas","Fisica","Quimica","Historia","Lingua"]
    notas = []
    for materia in materias:
        nota = input(f"Indica la nota que sacaste en: {materia}\n")
        notas.append(nota)
    for index,nota in enumerate(notas):
        print(f"Tu nota en {materias[index]} es {nota}")
          
        