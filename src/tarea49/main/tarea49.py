from luhn import luhn


class Persona:

    def __init__(self, nombre, user, passwd, tarjeta):
        self.nombre = nombre
        self.user = user
        self.passwd = passwd
        self.tarjeta = tarjeta

    def get_tarjeta(self):
        return self._tarjeta

    def set_tarjeta(self, numtarjeta):
        if luhn(numtarjeta):
            self._tarjeta = numtarjeta
        else:
            raise ValueError("Número invalido")

    tarjeta = property(get_tarjeta, set_tarjeta)


if __name__ == "__main__":
    nombre = input("Introduce tu nombre\n")
    user = input("Introduce tu usuario\n")
    password = input("Introduce tu contraseña\n")
    tarjeta = input("Introduce tu numero de tarjeta\n")
    usuario = Persona(nombre, user, password, tarjeta)
    usuario.tarjeta = "344"
    if luhn(usuario.tarjeta):
        print("Numero valido")
    else:
        print("Numero invalido")
