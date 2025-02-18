# Käyttöliittymä.
def kysy_pelaajat():
    """Kysyy pelaajien nimet ja palauttaa ne listana."""
    pelaajat = input("Syötä pelaajien nimet pilkulla eroteltuna: ").split(',')
    return [pelaaja.strip() for pelaaja in pelaajat if pelaaja.strp()]

def nayta_pelitilanne(peli):
    """Näyttää pelitilanteen, kuten pisteet ja kierroksen."""
    print(f"\nKierros {peli.kierros}")
    for pelaaja, pisteet in peli.pisteet.items():
        print(f"{pelaaja}: {pisteet} pistettä")

def nayta_voittaja(peli):
    """Näyttää pelin voittajan ja pisteet."""
    voittaja, pisteet = peli.hae_voittaja()
    print(f"\n {voittaja} voitti {pisteet} pisteellä!")

def kysy_jatketaanko():
    """Kysyy pelaajalta, haluavatko he jatkaa peliä."""
    return input("Haluatko jatkaa peliä? (kyllä/ei): ")