if __name__=="__main__":
    materias = ["Matematicas","Fisica","Quimica","Historia","Lingua"]
    notas = []
    for materia in materias:
        nota = input(f"Indica la nota que sacaste en: {materia}\n")
        nota = int(nota)
        notas.append(nota)   
    for index,nota in enumerate(notas):
        if nota<5:
            print(f"Tienes que repetir {materias[index]} por que sacaste un {nota}")