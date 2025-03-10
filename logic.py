import random

class YatzyPeli:
    def __init__(self):
        self.nopat = [0] * 5
        self.pisteet = {1: 0, 2: 0}
        self.nykyinen_pelaaja = 1
        self.kierros = 1
        self.broskut = 0
        self.kategoriat = {
            1: {
                "set": None,
                "kare": None,
                "full_house": None,
                "mali_street": None,
                "suuri_street": None,
                "schanssi": None,
                "yatzy": None,
            },
            2: {
                "set": None,
                "kare": None,
                "full_house": None,
                "mali_street": None,
                "suuri_street": None,
                "schanssi": None,
                "yatzy": None,
            },
        }
        for i in range(1, 7):
            self.kategoriat[1][str(i)] = None
            self.kategoriat[2][str(i)] = None

    def heita_nopat(self, pidettavat=None):
        if self.broskut >= 3:
            print("Olet jo heittänyt 3 kertaa! Valitse kategoria.")
            return

        if pidettavat:
            uudet_nopat = [random.randint(1, 6) if i not in pidettavat else self.nopat[i] for i in range(5)]
        else:
            uudet_nopat = [random.randint(1, 6) for _ in range(5)]

        self.nopat = uudet_nopat
        self.broskut += 1
        print(f"Pelaaja {self.nykyinen_pelaaja} heitti: {self.nopat} (heitto {self.broskut}/3)")

    def laske_pisteet_kategoria(self, silmaluku):
        return sum(n for n in self.nopat if n == silmaluku)

    def onko_set(self):
        return any(self.nopat.count(n) >= 3 for n in set(self.nopat))

    def onko_kare(self):
        return any(self.nopat.count(n) >= 4 for n in set(self.nopat))

    def onko_full_house(self):
        return sorted([self.nopat.count(n) for n in set(self.nopat)]) == [2, 3]

    def onko_street(self, suuri=False):
        mahdolliset = {tuple(sorted(street)) for street in [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]}
        if suuri:
            return tuple(sorted(set(self.nopat))) in mahdolliset
        return any(set(street).issubset(self.nopat) for street in [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)])

    def onko_ytzi(self):
        return len(set(self.nopat)) == 1

    def laske_bonus(self):
        ykkosista_kuutosiin = sum(v for k, v in self.kategoriat[self.nykyinen_pelaaja].items() if k in "123456" and v is not None)
        return 50 if ykkosista_kuutosiin >= 63 else 0

    def aseta_pisteet(self, kategoria):
        if self.kategoriat[self.nykyinen_pelaaja][kategoria] is not None:
            print("Tämä kategoria on jo käytetty! Valitse toinen.")
            return False

        if kategoria in "123456":
            pisteet = self.laske_pisteet_kategoria(int(kategoria))
        elif kategoria == "set" and self.onko_set():
            pisteet = sum(self.nopat)
        elif kategoria == "kare" and self.onko_kare():
            pisteet = sum(self.nopat)
        elif kategoria == "full_house" and self.onko_full_house():
            pisteet = 25
        elif kategoria == "mali_street" and self.onko_street(suuri=False):
            pisteet = 30
        elif kategoria == "suuri_street" and self.onko_street(suuri=True):
            pisteet = 40
        elif kategoria == "schanssi":
            pisteet = sum(self.nopat)
        elif kategoria == "yatzy" and self.onko_ytzi():
            pisteet = 50
        else:
            print("Tämä kategoria ei täsmää nykyisiin noppalukuihin.")
            return False

        self.kategoriat[self.nykyinen_pelaaja][kategoria] = pisteet
        self.pisteet[self.nykyinen_pelaaja] += pisteet

        bonus = self.laske_bonus()
        if bonus > 0:
            self.pisteet[self.nykyinen_pelaaja] += bonus
            print(f"Pelaaja {self.nykyinen_pelaaja} sai 50 bonuspistettä!")

        print(f"Pisteet lisätty: {pisteet} pistettä kategoriaan {kategoria}")
        return True

    def vaihda_pelaaja(self):
        self.nykyinen_pelaaja = 1 if self.nykyinen_pelaaja == 2 else 2
        self.kierros += 1
        print(f"Vuoro vaihtui. Nyt pelaa pelaaja {self.nykyinen_pelaaja}.")

    def pelaa_kierros(self):
        self.broskut = 0
        self.heita_nopat()

        while self.broskut < 3:
            valinta = input("Haluatko heittää uudestaan? (k/e) tai lopettaa pelin kirjoittamalla 'end': ").strip().lower()
            if valinta == "k":
                pidettavat = input("Anna pidettävien noppien indeksit (esim. 0,2,4) tai jätä tyhjäksi: ").strip()
                pidettavat = [int(i) for i in pidettavat.split(",") if i.isdigit()]
                self.heita_nopat(pidettavat)
            elif valinta == "end":
                print("Peli lopetettu ennenaikaisesti.")
                return False
            else:
                break

        while True:
            print("\nValitse kategoria:")
            available_categories = [k for k, v in self.kategoriat[self.nykyinen_pelaaja].items() if v is None]
            print(", ".join(available_categories))
            valinta = input("Kirjoita kategoria: ").strip().lower()

            if valinta in available_categories and self.aseta_pisteet(valinta):
                break
            else:
                print(f"Virheellinen valinta! Valitse yksi seuraavista: {', '.join(available_categories)}")

        self.vaihda_pelaaja()
        return True

    def lopeta_peli(self):
        print("\nPeli päättyi! Lopputulokset:")
        for pelaaja, pisteet in self.pisteet.items():
            print(f"Pelaaja {pelaaja}: {pisteet} pistettä")
        
        if self.pisteet[1] > self.pisteet[2]:
            print("Pelaaja 1 voitti!")
        elif self.pisteet[2] > self.pisteet[1]:
            print("Pelaaja 2 voitti!")
        else:
            print("Peli päättyi tasapeliin!")

    def onko_peli_paattynyt(self):
        return all(v is not None for v in self.kategoriat[1].values()) and all(v is not None for v in self.kategoriat[2].values())

if __name__ == "__main__":
    peli = YatzyPeli()
    while not peli.onko_peli_paattynyt():
        if not peli.pelaa_kierros():
            break

    peli.lopeta_peli()
