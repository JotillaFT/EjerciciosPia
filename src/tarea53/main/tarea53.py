import random
import os

def clear():
    if os.name =='nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

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
    def resultado(self):
        if self.puntosBanca > 21 and self.puntosJugador <=21:
            return True
        elif self.puntosJugador > self.puntosBanca and self.puntosJugador <= 21:
            return True
        elif self.puntosBanca > self.puntosJugador and self.puntosBanca <= 21:
            return False
        elif self.puntosJugador == self.puntosBanca:
            return False
        elif self.puntosBanca < self.puntosJugador and self.puntosJugador > 21:
            return False


if __name__ == "__main__":
    clear()
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
            while blackjack.puntosBanca < blackjack.puntosJugador:
                blackjack.banca.append(blackjack.sacarCarta())
                blackjack.puntosBanca = blackjack.calcPuntos(blackjack.banca)
            break
    if blackjack.resultado():
        print(f"El jugador tiene {blackjack.jugador} y gana con {blackjack.puntosJugador} puntos mientras que la banca tiene {blackjack.banca} siendo estos {blackjack.puntosBanca} puntos")
    else: 
        print(f"El jugador tiene {blackjack.jugador} y pierde con {blackjack.puntosJugador} puntos mientras que la banca tiene {blackjack.banca} siendo estos {blackjack.puntosBanca} puntos")
