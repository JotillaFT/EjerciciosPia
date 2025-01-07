from luhn import luhn
from dataclasses import dataclass

class Tarjeta:
    def __init__(self,numero):
        if luhn(numero):
            self.numero = numero
        else:
            raise ValueError("Número invalido")
    def __str__(self):
        return f"{self.numero}"

@dataclass(frozen = True)
class Persona():
    nombre : str 
    apellidos : str 
    nombre_completo : str 
    user : str 
    passwd: str 
    tarjeta : Tarjeta 
  
if __name__ == "__main__":
    #nombre = input("Introduce tu nombre\n")
    nombre = "Josue"
    #apellido = input("Introduce tu apellido\n")
    apellido = "Fontan"
    nombre_completo = f"{nombre} {apellido}"
    #user = input("Introduce tu usuario\n")
    user = "Jotilla"
    #password = input("Introduce tu contraseña\n")
    password = "vnsjghjgs"
    #numero = input("Introduce tu numero de tarjeta\n")
    numero = "584929217191"
    usuario = Persona(nombre,apellido,nombre_completo, user, password, Tarjeta(numero))
    print(usuario)
    print(usuario.tarjeta)
