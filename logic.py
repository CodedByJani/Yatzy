import random

class YatzyPeli:
    def __init__(self):
        # Alustetaan peliin liittyvät arvot, kuten nopat ja pisteet
        self.nopat = [0] * 5  # Viisi noppaa pelissä
        self.pisteet = {1: 0, 2: 0}  # Kaksi pelaajaa, kummallekin nollapisteet
        self.nykyinen_pelaaja = 1  # Aloittaa pelaaja 1
        self.kierros = 1  # Ensimmäinen kierros
        self.broskut = 0

        self.kategoriat = {
            1: {  # Pelaaja 1 kategorian pisteet
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
            2: {  # Pelaaja 2 kategorian pisteet
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

    def kysy_pelaajien_nimet(self):
        self.pelaajat = {
            1: input("Anna ensimmäisen pelaajan nimi: ").strip() or "Pelaaja 1",
            2: input("Anna toisen pelaajan nimi: ").strip() or "Pelaaja 2",
        }

    def tulosta_pelaajan_nimi(self):
        return self.pelaajat[self.nykyinen_pelaaja]

    def heita_nopat(self, pidettavat=None):
        if self.broskut >= 3:  # Kolme heittoa on jo suoritettu
            print("Olet jo heittänyt 3 kertaa! Valitse kategoria.")
            return

        if pidettavat:
            # Jos käyttäjä valitsee pidettävät nopat, ne pysyvät ja muut heitetään uudelleen
            uudet_nopat = [random.randint(1, 6) if i not in pidettavat else self.nopat[i] for i in range(5)]
        else:
            # Muutoin heitetään kaikki nopat
            uudet_nopat = [random.randint(1, 6) for _ in range(5)]

        self.nopat = uudet_nopat  # Päivitetään nopat
        self.broskut += 1  # Kasvatetaan heittojen laskuria
        print(f"{self.tulosta_pelaajan_nimi()} heitti: {self.nopat} (heitto {self.broskut}/3)")

    def laske_pisteet_kategoria(self, silmaluku):
        # Laskee pisteet valitulle silmäluvulle (esim. "ykköset")
        return sum(n for n in self.nopat if n == silmaluku)

    def onko_yksi_pari(self):
        # Tarkistaa, onko heitoissa yksi pari
        return any(self.nopat.count(n) == 2 for n in set(self.nopat))

    def onko_kaksi_paria(self):
        # Tarkistaa, onko heitoissa kaksi paria
        return len([n for n in set(self.nopat) if self.nopat.count(n) == 2]) == 2

    def onko_kolmoisluku(self):
        # Tarkistaa, onko heitoissa kolmonen (kolme samaa silmälukua)
        return any(self.nopat.count(n) >= 3 for n in set(self.nopat))

    def onko_neloisluku(self):
        # Tarkistaa, onko heitoissa neloset (neljä samaa silmälukua)
        return any(self.nopat.count(n) >= 4 for n in set(self.nopat))

    def onko_pieni_suora(self):
        # Tarkistaa, onko heitoissa pieni suora (1,2,3,4,5)
        return set(self.nopat).issubset({1, 2, 3, 4, 5})

    def onko_suuri_suora(self):
        # Tarkistaa, onko heitoissa suuri suora (2,3,4,5,6)
        return set(self.nopat).issubset({2, 3, 4, 5, 6})

    def onko_täyskäsi(self):
        # Tarkistaa, onko heitoissa täyskäsi (kolmonen ja pari)
        return sorted([self.nopat.count(n) for n in set(self.nopat)]) == [2, 3]

    def onko_sattuma(self):
        # Sattumassa ei ole tarkistusta, vaan aina palautetaan True
        return True

    def onko_yatzy(self):
        # Tarkistaa, onko heitoissa Yatzy (viisi samanlaista silmälukua)
        return len(set(self.nopat)) == 1

    def laske_bonus(self):
        # Laskee mahdollisen bonuspisteen (50 pistettä, jos on saatu tarpeeksi korkeita lukuja)
        ykkosista_kuutosiin = sum(v for k, v in self.kategoriat[self.nykyinen_pelaaja].items() if k in "123456" and v is not None)
        return 50 if ykkosista_kuutosiin >= 63 else 0

    def aseta_pisteet(self, kategoria):
        # Määrittää pelaajan pisteet valitulle kategoriassa
        if self.kategoriat[self.nykyinen_pelaaja][kategoria] is not None:
            print("Tämä kategoria on jo käytetty! Valitse toinen.")
            return False

        nopat_lajiteltu = sorted(self.nopat, reverse=True)  # Järjestetään nopat suurimmasta pienimpään
        pisteet = 0  # Oletuksena 0 pistettä, jos ei löydy yhteensopivaa yhdistelmää

        # Kategorian tarkistus ja pisteiden laskeminen
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

        self.kategoriat[self.nykyinen_pelaaja][kategoria] = pisteet  # Päivitetään kategoriaan saatu pistemäärä
        self.pisteet[self.nykyinen_pelaaja] += pisteet  # Lisätään pisteet pelaajan kokonaispisteisiin

        bonus = self.laske_bonus()  # Tarkistetaan mahdollinen bonus
        if bonus > 0:
            self.pisteet[self.nykyinen_pelaaja] += bonus
            print(f"Pelaaja {self.nykyinen_pelaaja} sai 50 bonuspistettä!")

        print(f"Pisteet lisätty: {pisteet} pistettä kategoriaan {kategoria}")
        return True

    def vaihda_pelaaja(self):
        # Vaihdetaan pelaajaa vuorotellen
        self.nykyinen_pelaaja = 1 if self.nykyinen_pelaaja == 2 else 2
        self.kierros += 1
        print(f"Vuoro vaihtui. Nyt pelaa {self.tulosta_pelaajan_nimi()}.")

    def pelaa_kierros(self):
        # Yksi pelikierros, sisältäen nopan heiton ja kategorian valinnan
        self.broskut = 0
        self.heita_nopat()

        while self.broskut < 3:  # Pelaaja voi heittää enintään kolme kertaa
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
            # Kategorian valinta ja pisteiden asettaminen
            print("\nValitse kategoria:")
            available_categories = [k for k, v in self.kategoriat[self.nykyinen_pelaaja].items() if v is None]
            print(", ".join(available_categories))
            valinta = input("Kirjoita kategoria: ").strip().lower()

            if valinta in available_categories and self.aseta_pisteet(valinta):
                break
            else:
                print(f"Virheellinen valinta! Valitse yksi seuraavista: {', '.join(available_categories)}")

        self.vaihda_pelaaja()  # Vaihdetaan pelaajaa kierroksen jälkeen
        return True

    def lopeta_peli(self):
        # Pelin lopettaminen ja loppupisteiden näyttäminen
        print("\nPeli päättyi! Lopputulokset:")
        for pelaaja, pisteet in self.pisteet.items():
            pelaajan_nimi = self.pelaajat.get(pelaaja, f"Pelaaja {pelaaja}")
            print(f"{pelaajan_nimi}: {pisteet} pistettä")
        
        if self.pisteet[1] > self.pisteet[2]:
            print(f"{self.pelaajat[1]} voitti!")
        elif self.pisteet[2] > self.pisteet[1]:
            print(f"{self.pelaajat[2]} voitti!")
        else:
            print("Peli päättyi tasapeliin!")
        return True


    def onko_peli_paattynyt(self):
        return all(v is not None for v in self.kategoriat[1].values()) and all(v is not None for v in self.kategoriat[2].values())

if __name__ == "__main__":
    peli = YatzyPeli()
    peli.kysy_pelaajien_nimet()
    while not peli.onko_peli_paattynyt():
        if not peli.pelaa_kierros():
            break

    peli.lopeta_peli()
    