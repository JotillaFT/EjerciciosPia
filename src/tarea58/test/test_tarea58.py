from main.tarea58 import Alien,new_aliens_collection,Decorador,EscudoCombateDecorador,EscudoPersonalDecorador
def test_alien():
    Alien(4,2)
    assert Alien.alien_count == 1
    
def test_collection_aliens():
    listaAliens = new_aliens_collection([(4, 7),(-1, 0),(4, 7),(-1, 0),(4, 7),(-1, 0),(4, 7),(-1, 0)])
    assert len(listaAliens) == 8
    
def test_hit():
    alien1 = Alien(7,8)
    alien2 = Alien(7,8)
    alien3 = Alien(7,8)
    alien1 = EscudoPersonalDecorador(alien1)
    alien2 = EscudoCombateDecorador(alien2)
    alien3 = EscudoCombateDecorador(alien3)
    alien1.hit(3)
    alien2.hit(1)
    alien3.hit()
    assert alien1.alien.lives == 1
    assert alien2.alien.lives == 3
    assert alien3.alien.lives == 3
    
    