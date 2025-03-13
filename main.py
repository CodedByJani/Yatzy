import random
from ui import pelin_aloitus, pelin_tulos
from logic import YatzyPeli

def main():
    peli = YatzyPeli()
    
    pelin_aloitus()
    while not peli.onko_peli_paattynyt():
        if not peli.pelaa_kierros():
            break

    pelin_tulos(peli.pisteet)

if __name__ == "__main__":
    main()