import sqlite3

db = sqlite3.connect("testi.db")
db.isolation_level = None

db.execute("CREATE TABLE Tuotteet (id INTEGER PRIMARY KEY, nimi TEXT, hinta INTEGER)")

db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES ('selleri', 5)")
db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES ('nauris', 8)")
db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES ('lanttu', 4)")

tuotteet = db.execute("SELECT nimi, hinta FROM Tuotteet").fetchall()
print(tuotteet)

hinta = db.execute("SELECT MAX(hinta) FROM Tuotteet").fetchone()
print(hinta)

#koodi kysyy käyttäjältä tuotteen nimeä ja ilmoittaa sitten tuotteen hinnan tai tiedon 
#siitä, että tuotetta ei ole tietokannassa.

nimi = input("Tuotteen nimi: ")
#get the first match, nimi=? meinaa ett voi pistää oman parametrin
hinta = db.execute("SELECT hinta FROM Tuotteet WHERE nimi=?", [nimi]).fetchone() 
if hinta:
    print("Hinta on", hinta[0])
else:
    print("Ei löytynyt")

#add a product to the database 
nimi = input("Tuotteen nimi: ")
hinta = input("Tuotteen hinta: ")
db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES (?, ?)", [nimi, hinta])

print(db.execute("select * from tuotteet").fetchall())
#show the added products id
print(db.execute("select * from tuotteet").lastrowid)

