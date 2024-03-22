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


class romuralli:
    tunnit = 0

    def __init__(self,nimi, kilometri_maara, autojen_maara):
        self.nimi = nimi
        self.autot = []
        self.kilometri_maara = kilometri_maara
        self.autot_lisaa(autojen_maara)

    def kilpailu_ohi(self):
        for i in self.autot:
            if i.kuljettu_matka >= self.kilometri_maara:
                return False
        return True

    def tulosta_tilanne(self):
        viimeinen_indexi = len(self.autot) - 1

        for indexi, i in enumerate(self.autot):
            if self.kilpailu_ohi() == False:
                if i.kuljettu_matka > self.kilometri_maara:
                    print(f"{i.rekisteritunnus:7} | {i.kuljettu_matka:7}km | {i.nopeus:4} km/h | {i.huippunopeus:4} km/h *")
                else:
                    print(f"{i.rekisteritunnus:7} | {i.kuljettu_matka:7}km | {i.nopeus:4} km/h | {i.huippunopeus:4} km/h")
            elif romuralli.tunnit % 10 == 0:
                print(f"{i.rekisteritunnus:7} | {i.kuljettu_matka:7}km | {i.nopeus:4} km/h | {i.huippunopeus:4} km/h")

            if indexi == viimeinen_indexi and romuralli.tunnit % 10 == 0:
                print("-" * 43)
        romuralli.tunnit += 1

    def autot_lisaa(self, autojen_maara):
        for i in range(autojen_maara):
            self.autot.append(Auto(f"abc-{i}", np.random.randint(100, 200)))

    def jatka(self):
        for i in self.autot:
            i.kiihdyta()
            i.kulje(1)
        self.tulosta_tilanne()
        return self.kilpailu_ohi()

def main():
    kilpailu = romuralli("Suuri romuralli",8000, 10)

    jatka = True

    while jatka == True:
        jatka = kilpailu.jatka()



if __name__ == "__main__":
    main()
