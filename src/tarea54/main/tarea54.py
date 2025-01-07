import re

class Personaje:

    def __init__(self,name,height,mass,hair_color,skin_color,eye_color,birdth_year,sex,gender,homeworl,species,films):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birdth_year = birdth_year
        self.sex = sex
        self.gender = gender
        self.homeworl = homeworl
        self.species = species
        self.films = films

    def __str__(self):
        # Obtener el nombre de la clase
        class_name = self.__class__.__name__
        # Obtener los atributos de la clase
        # Podemos agregar saltos de línea y espacios para imprimirlos de forma más organizada
        attributes = "\n    " + "\n    ".join([f"{attr} = {getattr(self, attr)!r}" for attr in self.__dict__])
        return f"{class_name}({attributes})"

    def __repr__(self):
    # Obtener el nombre de la clase
        class_name = self.__class__.__name__
    # Obtener los atributos de la clase
        attributes = ', '.join([f'{attr}={getattr(self, attr)!r}' for attr in self.dict])
        return f"{class_name}({attributes})"

if __name__ == "__main__":
    cont = 0
    personajes = []
    with open("starwars.csv","r") as datos:
        header = datos.readline()
        for biologico in datos:
                personajes.append(Personaje(re.split(r',(?=(?:[^"]"[^"]")[^"]$)', biologico.strip())))
    for i in range(len(personajes)):
        if (personajes[i].species == "Droid"):
            print(personajes[i])