def pelin_aloitus():
    print("Tervetuloa pelaamaan Yatzy-peliä!")
    print("Peli alkaa, kun molemmat pelaajat ovat valmiita!")
    input("Paina Enter aloittaaksesi...")

def pelin_tulos(pisteet):
    print("\nPeli päättyi! Lopputulokset:")
    for pelaaja_numero, pelaajan_pisteet in pisteet.items():
        print(f"Pelaaja {pelaaja_numero}: {pelaajan_pisteet} pistettä")
    
    if pisteet[1] > pisteet[2]:
        print("Pelaaja 1 voitti!")
    elif pisteet[2] > pisteet[1]:
        print("Pelaaja 2 voitti!")
    else:
        print("Peli päättyi tasapeliin!")