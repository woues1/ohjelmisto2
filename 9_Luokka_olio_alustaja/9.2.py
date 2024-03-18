class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus: str = rekisteritunnus
        self.huippunopeus: int = huippunopeus
        self.nopeus: int = 0
        self.kuljettu_matka: int = 0

    def kiihdyta(self, nopeus):
        if self.nopeus + nopeus < 0:
            self.nopeus = 0
        elif self.nopeus + nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus + nopeus

auto = Auto("ABC-123", 142)
auto.kiihdyta(+30)
print(auto.nopeus)
auto.kiihdyta(+70)
print(auto.nopeus)
auto.kiihdyta(+50)
print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)