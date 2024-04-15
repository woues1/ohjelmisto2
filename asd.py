# Mitä seuraava koodi tulostaa?

class Henkilo:

    def __init__(self, nimi="Bob"):
        self.nimi = nimi
        self.ika = 20
        self.pituus = 170

    def vanhene(self, ika):
        self.ika += ika

    def muuta_pituutta(self, pituus=10):
        self.pituus = pituus

    def get_nimi(self):
        return self.nimi

    def get_data(self):
        return [self.pituus, self.ika]


class Parisuhde:
    def __init__(self, henkilo1, henkilo2):
        self.kumppani1 = henkilo1
        self.kumppani2 = henkilo2

    def ilmoita_suhde(self):
        print(
            self.kumppani1.get_nimi() + " ja " + self.kumppani2.get_nimi() + " ovat suhteessa."
        )


a = Henkilo()
b = Henkilo("Boberetta")

parisuhde = Parisuhde(a, b)

parisuhde.ilmoita_suhde()

parisuhde.kumppani3 = parisuhde.kumppani1

parisuhde.kumppani2 = parisuhde.kumppani1

parisuhde.kumppani1 = Henkilo("Bobette")

parisuhde.ilmoita_suhde()

# Vastaus
# ->
# ->