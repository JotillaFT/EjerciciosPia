def new_aliens_collection(posiciones_iniciales):
    # aliens = []
    # for posiciones in posiciones_iniciales:
    #     aliens.append(Alien(posiciones[0],posiciones[1]))
    # return aliens
    return [Alien(posiciones[0], posiciones[1]) for posiciones in posiciones_iniciales]


class Alien:
    alien_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        Alien.alien_count += 1

    def hit(self, hits=1):
        self.lives = self.lives - hits

    def is_alive(self):
        return self.lives <= 0

    def tp(self, x, y):
        self.x = x
        self.y = y

    def colisionar(self, obj):
        pass


class Decorador(Alien):
    _alien: Alien = None

    def __init__(self, alien: Alien) -> None:
        self._alien = alien

    @property
    def alien(self) -> Alien:
        return self._alien

    def hit(self, hits=1):
        return self._alien.hit(hits)

    def is_alive(self):
        return self._alien.is_alive()

    def tp(self, x, y):
        return self._alien.tp(x, y)

    def colisionar(self, obj):
        return self.colisionar(obj)


class EscudoPersonalDecorador(Decorador):
    def __init__(self, alien: Alien) -> None:
        super().__init__(alien)
        self.durabilidad = 5

    def hit(self, hits=1):
        self.durabilidad -= 1
        if self.durabilidad >= 0:
            return self._alien.hit(hits - 1)
        else:
            return self._alien.hit(hits)


class EscudoCombateDecorador(Decorador):
    def __init__(self, alien: Alien) -> None:
        super().__init__(alien)
        self.durabilidad = 20

    def hit(self, hits=1):
        if self.durabilidad > 0:
            if hits <= 5:
                self.durabilidad -= hits
                hits = 0
            else:
                self.durabilidad -= 5
                hits -= 5
            
                return self._alien.hit(hits)
        else:
            return self._alien.hit(hits)


if __name__ == "__main__":
    aliens = new_aliens_collection([(4, 7), (-1, 0)])
    aliens[0] = EscudoPersonalDecorador(aliens[0])
    aliens[1] = EscudoCombateDecorador(aliens[1])
    aliens[0].hit(2)
    aliens[1].hit(5)
    for alien in aliens:
        print(alien.alien.lives)
        print(alien.durabilidad)
    
        
    
