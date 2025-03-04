# 🎲 Yatzy 🎲

Tämä on konsolipohjainen Yatzy-peli, joka on toteutettu Pythonilla.  
Peli sisältää noppien heiton, pistelaskennan ja vuorojärjestelmän.

## 📜 Säännöt

Peli perustuu klassisen Yatzyn sääntöihin:
- Jokaisella pelaajalla on 3 heittoa per kierros.
- Pelaaja voi valita, mitkä nopat pitää ja mitkä heittää uudestaan.
- Pisteytys perustuu Yatzy-sääntöihin.
- Pelin lopussa eniten pisteitä saanut voittaa! 🏆

📂 Projektin rakenne:

yatzy/
│
├── .gitignore    # Tiedostot, joita Git ei seuraa.
├── main.py       # Pääohjelma, joka käynnistää pelin.
├── logic.py      # Pelilogiikka (nopan heitto, pisteiden laskenta, vuorot).
├── ui.py         # Käyttöliittymä ja vuorovaikutus pelaajan kanssa.
├── README.md     # Tämä tiedosto – projektin kuvaus ja ohjeet.

## Käyttöohjeet:

1️⃣ Varmista, että sinulla on Python asennettuna
Tarkista Pythonin versio komennolla:
python --version
Jos Pythonia ei ole asennettu, voit ladata sen täältä.

2️⃣ Lataa ja käynnistä peli
Kloonaa projekti GitHubista:
git clone <repository_url>
cd yatzy

Käynnistä peli komennolla:
python main.py

👨‍💻 Kehittäjät
👤 Daniil – Pelilogiikka & pistelaskenta
👤 Jani – Käyttöliittymä & pääohjelma

# Työnjako:
(Daniil)
Pelilogiikka ja pistelaskenta (logic.py).
Siihen kuuluisi:
Noppien hallinta: nopan heitto
Pistelaskujärjestelmä: Yatzy-säännöt ja pisteytys.
Vuorojärjestelmä: Kuka on vuorossa ja kuinka monta heittoa per kierros

 (Jani)
Käyttöliittymä ja peliin liittyvä vuorovaikutus (ui.py & main.py)
siihen kuuluu:
Tulostukset ja käyttöliittymä: Näytä tulokset ja valikot konsolissa.
Pelaajien valinnat: Kysy käyttäjältä, mitä hän haluaa tehdä (heitto, pisteytys).
Pelin käynnistys: main.py yhdistää kaiken yhteen.

https://cardgames.io/yahtzee/