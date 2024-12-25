class ADN():
    def __init__(self,cadena):
            self.cadena = cadena
        
    def __sub__(self,adn2):
        hamm = 0
        if len(self.cadena) == len(adn2.cadena):
            for a,b in zip(self.cadena,adn2.cadena):
                if a!= b:
                    hamm +=1
        else:
            raise ValueError("Distancia de cadenas distintas")
        return hamm
    
if __name__ == "__main__":
    exveemon = ADN("GAGCCTACTAACGGGA")
    stingmon = ADN("CATCGTAATGACGGCCT")
    print(exveemon-stingmon)