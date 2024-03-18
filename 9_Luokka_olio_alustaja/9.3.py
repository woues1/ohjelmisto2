class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus: str = rekisteritunnus
        self.huippunopeus: int = huippunopeus
        self.nopeus: float = 0
        self.kuljettu_matka: float = 0

    def kiihdyta(self, nopeus):
        if self.nopeus + nopeus < 0:
            self.nopeus = 0
        elif self.nopeus + nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus + nopeus
    def kulje(self, aika):
        self.kuljettu_matka = aika * self.nopeus

auto = Auto("ABC-123", 142)
auto.kiihdyta(+30)
print(auto.nopeus)
auto.kiihdyta(+70)
print(auto.nopeus)
auto.kiihdyta(+50)
auto.kulje(1.5)
print(f"{auto.kuljettu_matka} km")
print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)