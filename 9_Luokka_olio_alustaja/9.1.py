class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def tiedot(self):
        print(f"Rekisteritunnus {self.rekisteritunnus} \n"
              f"Huippunopeus {self.huippunopeus} \n"
              f"nopeus {self.nopeus} \n"
              f"Kuljettu matka {self.kuljettu_matka} \n")


auto = Auto("ABC-123", 142)

auto.tiedot()