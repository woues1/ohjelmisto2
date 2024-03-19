"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""

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

    def __init__(self, kilometri_maara, autojen_maara):
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


kilpailu = romuralli(8000, 10)


jatka = True
while jatka == True:
    kilpailu.jatka()
    jatka = kilpailu.kilpailu_ohi()
    kilpailu.tulosta_tilanne()
