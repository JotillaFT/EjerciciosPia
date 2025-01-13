

from blackjack.xogo import Xogo, Xogador, EstratexiaDoNumero15

if __name__ == "__main__":
    xogo = Xogo()
    xogo.addXogador(Xogador("Xogador1"))
    xogo.addXogador(Xogador("Xogador2"))
    maquina = Xogador("Maquina")
    maquina.estratexia = EstratexiaDoNumero15()
    xogo.addXogador(maquina)
    xogo.xogar()
