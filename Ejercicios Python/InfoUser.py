if __name__ == "__main__":
    nombre = input("Indica tu nombre\n")
    edad = input("Indica tu edad\n")
    direccion = input("Indica tu direccion\n")
    tlf = input("Indica tu numero de telefono\n")
    usuario = {"nombre":nombre,"edad":edad,"direccion":direccion,"tlf":tlf}
    print(f"{usuario['nombre']} ten {usuario['edad']} anos, vive en {usuario['direccion']} e o seu número de telefono é {usuario['tlf']}")