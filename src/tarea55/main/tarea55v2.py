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
    
    # def __init__(self, nombre,apellidos,nombre_completo, user, passwd, tarjeta):
    #     self.nombre = nombre
    #     self.apellidos = apellidos
    #     self.nombre_completo = nombre_completo
    #     self.user = user
    #     self.passwd = passwd
    #     if luhn(tarjeta):
    #         self._tarjeta = tarjeta
    #     else:
    #         raise ValueError("Número invalido")
        
    # def __post_init__(self):
    #     self.nombre_completo = f"{self.nombre} {self.apellidos}"
    #     if luhn(self.tarjeta):
    #         self._tarjeta = self.tarjeta
    #     else:
    #         raise ValueError("Número invalido")

   


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
    usuario.tarjeta = "344"
    if luhn(usuario.tarjeta):
        print("Numero valido")
    else:
        print("Numero invalido")
