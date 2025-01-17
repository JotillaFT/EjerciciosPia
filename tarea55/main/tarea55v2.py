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
    
    def get_tarjeta(self):
        return self._numero

    def set_tarjeta(self, numtarjeta):
        if luhn(numtarjeta):
            self._numero = numtarjeta
        else:
            raise ValueError("Número invalido")

    tarjeta = property(get_tarjeta, set_tarjeta)

@dataclass
class Persona():
    nombre : str 
    apellidos : str 
    nombre_completo : str 
    user : str 
    passwd: str 
    tarjeta : Tarjeta 
    
if __name__ == "__main__":
    nombre = "Josue"
    apellido = "Fontan"
    nombre_completo = f"{nombre} {apellido}"
    user = "Jotilla"
    password = "vnsjghjgs"
    numero = "584929217191"
    usuario = Persona(nombre,apellido,nombre_completo, user, password, Tarjeta(numero))
    print(usuario)
    print(usuario.tarjeta)
    usuario.tarjeta = "344"
    if luhn(usuario.tarjeta):
        print("Numero valido")
    else:
        print("Numero invalido")
