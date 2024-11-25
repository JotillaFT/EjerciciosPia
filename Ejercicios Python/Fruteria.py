if __name__ == "__main__":
    frutas = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    fruta = input("Indica la fruta\n")
    fruta = fruta.title()
    if fruta in frutas:
        peso = input("Indica el peso de la fruta\n")
        peso = float(peso)
        precio = peso*frutas[fruta]
        print(f"EL coste de la fruta será: {precio}")
    else:
        print("No tenemos esa fruta")