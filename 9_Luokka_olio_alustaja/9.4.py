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

jatka = True
autot=[]
for i in range(1, 11):
    autot.append(Auto(f"abc-{i}", np.random.randint(100, 200)))

while jatka == True:
    for auto in autot:
        if auto.kuljettu_matka < 10000:
            auto.kulje(1)
            auto.kiihdyta()
        else:
            jatka = False

for auto in autot:
    if auto.kuljettu_matka >= 10000:
        print(f"voittaja: {auto.rekisteritunnus} {auto.kuljettu_matka} ")
    else:
        print(auto.rekisteritunnus, auto.kuljettu_matka)