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
                "ykköset": None,
                "kakkoset": None,
                "kolmoset": None,
                "neloset": None,
                "viitoset": None,
                "kuutoset": None,
                "yksi_pari": None,
                "kaksi_paria": None,
                "kolmoisluku": None,
                "neloisluku": None,
                "pieni_suora": None,
                "suuri_suora": None,
                "täyskäsi": None,
                "sattuma": None,
                "yatzy": None,
            },
            2: {
                "ykköset": None,
                "kakkoset": None,
                "kolmoset": None,
                "neloset": None,
                "viitoset": None,
                "kuutoset": None,
                "yksi_pari": None,
                "kaksi_paria": None,
                "kolmoisluku": None,
                "neloisluku": None,
                "pieni_suora": None,
                "suuri_suora": None,
                "täyskäsi": None,
                "sattuma": None,
                "yatzy": None,
            },
        }

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

    def onko_yksi_pari(self):
        return any(self.nopat.count(n) == 2 for n in set(self.nopat))

    def onko_kaksi_paria(self):
        return len([n for n in set(self.nopat) if self.nopat.count(n) == 2]) == 2

    def onko_kolmoisluku(self):
        return any(self.nopat.count(n) >= 3 for n in set(self.nopat))

    def onko_neloisluku(self):
        return any(self.nopat.count(n) >= 4 for n in set(self.nopat))

    def onko_pieni_suora(self):
        return set(self.nopat).issubset({1, 2, 3, 4, 5})

    def onko_suuri_suora(self):
        return set(self.nopat).issubset({2, 3, 4, 5, 6})

    def onko_täyskäsi(self):
        return sorted([self.nopat.count(n) for n in set(self.nopat)]) == [2, 3]

    def onko_sattuma(self):
        return True

    def onko_yatzy(self):
        return len(set(self.nopat)) == 1

    def laske_bonus(self):
        ykkosista_kuutosiin = sum(v for k, v in self.kategoriat[self.nykyinen_pelaaja].items() if k in "123456" and v is not None)
        return 50 if ykkosista_kuutosiin >= 63 else 0

    def aseta_pisteet(self, kategoria):
        if self.kategoriat[self.nykyinen_pelaaja][kategoria] is not None:
            print("Tämä kategoria on jo käytetty! Valitse toinen.")
            return False

        nopat_lajiteltu = sorted(self.nopat, reverse=True)
        pisteet = 0

        if kategoria == "ykköset":
            pisteet = self.laske_pisteet_kategoria(1)
        elif kategoria == "kakkoset":
            pisteet = self.laske_pisteet_kategoria(2)
        elif kategoria == "kolmoset":
            pisteet = self.laske_pisteet_kategoria(3)
        elif kategoria == "neloset":
            pisteet = self.laske_pisteet_kategoria(4)
        elif kategoria == "viitoset":
            pisteet = self.laske_pisteet_kategoria(5)
        elif kategoria == "kuutoset":
            pisteet = self.laske_pisteet_kategoria(6)
        elif kategoria == "yksi_pari":
            parit = [n for n in set(self.nopat) if self.nopat.count(n) >= 2]
            pisteet = max(parit) * 2 if parit else 0
        elif kategoria == "kaksi_paria":
            parit = sorted([n for n in set(self.nopat) if self.nopat.count(n) >= 2], reverse=True)
            pisteet = sum(parit[:2]) * 2 if len(parit) >= 2 else 0
        elif kategoria == "kolmoisluku":
            kolmoset = [n for n in set(self.nopat) if self.nopat.count(n) >= 3]
            pisteet = max(kolmoset) * 3 if kolmoset else 0
        elif kategoria == "neloisluku":
            neloset = [n for n in set(self.nopat) if self.nopat.count(n) >= 4]
            pisteet = max(neloset) * 4 if neloset else 0
        elif kategoria == "pieni_suora":
            pisteet = 15 if sorted(self.nopat) == [1, 2, 3, 4, 5] else 0
        elif kategoria == "suuri_suora":
            pisteet = 20 if sorted(self.nopat) == [2, 3, 4, 5, 6] else 0
        elif kategoria == "täyskäsi":
            parit = [n for n in set(self.nopat) if self.nopat.count(n) == 2]
            kolmoset = [n for n in set(self.nopat) if self.nopat.count(n) == 3]
            pisteet = sum(self.nopat) if parit and kolmoset else 0
        elif kategoria == "sattuma":
            pisteet = sum(self.nopat)
        elif kategoria == "yatzy":
            pisteet = 50 if self.onko_yatzy() else 0
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
                pidettavat = input("Anna pidettävien noppien indeksit (0,1,2,3,4) tai jätä tyhjäksi: ").strip()
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
    