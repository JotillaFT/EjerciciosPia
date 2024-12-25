class Vehiculo:
    def __init__(self,velMax,kms):
        self._velMax = velMax
        self._kms = kms

    def get_velMax(self):
        return self._velMax
    def set_velMax(self, vm):
        if vm > 0:
            self._velMax = vm
        else:
            raise ValueError("Dato no permitido")

    def get_kms(self):
        return self._kms
    def set_kms(self, kl):
        if kl > self.kms:
            self.kms = kl
        else:
            raise ValueError("Dato no permitido")

    velMax = property(get_velMax,set_velMax)
    kms = property(get_kms,set_kms)

    def __str__(self):
        return f"GUAU LOCO NI TORETO velocidad maxima: {self.velMax} y recorriste {self.kms}"
if __name__ == "__main":
    maxDestapler = Vehiculo(750,26000000)
    print(maxDestapler)