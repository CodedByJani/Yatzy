# Pääohjelma, josta peli käynnistetään.
import logic
import ui

def main():
    print("Tervetuloa pelaamaan Yatzya!")
    pelaajat = ui.kysy_pelaajat()
    peli = logic.YatzyPeli(pelaajat)

    while not peli.onko_peli_loppu():
        ui.nayta_pelitilanne(peli)
        peli.pelaa_vuorot()
    
    ui.nayta_voittaja(peli)

if __name__ == "__main__":
    main()