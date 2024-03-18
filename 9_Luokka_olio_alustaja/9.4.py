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

auto1 = Auto("abc-1",np.random.randint(100, 200))
auto2 = Auto("abc-2",np.random.randint(100, 200))
auto3 = Auto("abc-3",np.random.randint(100, 200))

while True:
    for auto in [auto1, auto2, auto3]:
        if auto.kuljettu_matka < 10000:
            auto.kulje(1)
            auto.kiihdyta()
        else:
            break

print(f"Auto: {auto1.rekisteritunnus} Kuljettu matka: {auto1.kuljettu_matka} \nAuto: {auto2.rekisteritunnus} Kuljettu matka: {auto2.kuljettu_matka} \nAuto: {auto3.rekisteritunnus} Kuljettu matka: {auto3.kuljettu_matka}")
