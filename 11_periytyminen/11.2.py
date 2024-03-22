import numpy as np


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus: str = rekisteritunnus
        self.huippunopeus: int = huippunopeus
        self.nopeus: float = 0
        self.kuljettu_matka: float = 0

    def kiihdyta(self):
        kiihdyta = np.random.randint(-10, +15)
        if self.nopeus + kiihdyta < 0:
            self.nopeus = 0
        elif self.nopeus + kiihdyta > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus + kiihdyta

    def kulje(self, aika):
        self.kuljettu_matka += aika*self.nopeus

    def tiedot(self):
        print(f"Rekisteritunnus {self.rekisteritunnus} \n"
              f"Huippunopeus {self.huippunopeus} \n"
              f"nopeus {self.nopeus} \n"
              f"Kuljettu matka {self.kuljettu_matka}")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self. akkukapasiteetti: float = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def tiedot(self):
        super().tiedot()
        print(f"Akkukapasiteetti {self.akkukapasiteetti} kw/h\n")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko: float = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)

    def tiedot(self):
        super().tiedot()
        print(f"Polttoaineen maara: {self.bensatankin_koko} l\n")


Autot = []
Autot.append(Sahkoauto("ABC-15", 180, 52.5))
Autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for auto in Autot:
    auto.nopeus = 80
    auto.kulje(3)
    auto.tiedot()