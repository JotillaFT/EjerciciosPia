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


if __name__ == "__main__":
    aliens = new_aliens_collection([(4, 7), (-1, 0)])
    for alien in aliens:
        print(alien.x, alien.y, alien.lives)
    aliens[0].hit(2)
    print(aliens[0].lives)