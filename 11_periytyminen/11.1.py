class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"nimi: {self.nimi}")


class Kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja} | sivumaara: {self.sivumaara}")


class Lehti(julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoittaja: {self.paatoimittaja}")
def main():
    julkaisut = []
    julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppa"))
    julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

    for julkaisu in julkaisut:
        julkaisu.tulosta_tiedot()

if __name__ == "__main__":
    main()