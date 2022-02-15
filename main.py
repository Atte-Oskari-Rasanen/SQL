import os 
os. chdir("/home/atte/Documents/SQL_course")

import tuotteet

print("1 - Lisää uusi tuote")
print("2 - Hae tuotteen hinta")
print("3 - Sulje ohjelma")

while True:
    komento = input("Anna komento: ")

    if komento == "1":
        nimi = input("Tuotteen nimi: ")
        hinta = input("Tuotteen hinta: ")
        tuotteet.lisaa_tuote(nimi, hinta)

    if komento == "2":
        nimi = input("Tuotteen nimi: ")
        hinta = tuotteet.hae_hinta(nimi)
        if hinta:
            print("Hinta on", hinta)
        else:
            print("Ei löytynyt")
    if komento == "3":
        break
    if komento == "4":
        tuotteet.kallein(nimi)