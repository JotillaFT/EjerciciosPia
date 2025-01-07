import random


class Blackjack:
    def __init__(self):
        self.baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
        self.jugador = []
        self.banca = []
        self.puntosJugador = 0
        self.puntosBanca = 0
        random.shuffle(self.baraja)

    def sacarCarta(self):
        carta = self.baraja[0]
        self.baraja.pop(0)
        return carta

    def prepararMesa(self):
        self.jugador.append(self.sacarCarta())
        self.jugador.append(self.sacarCarta())
        self.banca.append(self.sacarCarta())
        self.banca.append(self.sacarCarta())

    def mostrarMesa(self):
        self.puntosJugador = self.calcPuntos(self.jugador)
        self.puntosBanca = self.calcPuntos(self.banca)
        print(
            f"El jugador cuenta con {self.jugador} teniendo una puntuación de: {self.puntosJugador}"
        )
        print(f"La banca cuenta con {self.banca[0]} y '?'")

    def calcPuntos(self,cartas):
        puntos = 0
        for carta in cartas:
            if carta in ["J", "Q", "K"]:
               puntos += 10
            elif carta == "A":
                if puntos <= 9:
                   puntos += 11
                else:
                   puntos += 1
            else:
               puntos += int(carta)
        return puntos

    ##def jugarBanca(self):
        

if __name__ == "__main__":
    blackjack = Blackjack()
    blackjack.prepararMesa()
    blackjack.mostrarMesa()
    while blackjack.puntosJugador < 21:
        turno = input("Quiere el jugador otra carta? (s/n)")
        if turno == "s":
            blackjack.jugador.append(blackjack.sacarCarta())
            blackjack.puntosJugador = blackjack.calcPuntos(blackjack.jugador)
            blackjack.mostrarMesa()
        elif turno == "n":
            break
