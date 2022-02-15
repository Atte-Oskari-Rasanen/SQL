import sqlite3

db = sqlite3.connect("testi.db")
db.isolation_level = None

def lisaa_tuote(nimi, hinta):
    db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES (?,?)", [nimi, hinta])

def hae_hinta(nimi):
    hinta = db.execute("SELECT hinta FROM Tuotteet WHERE nimi=?", [nimi]).fetchone()
    if hinta:
        return hinta[0]
    else:
        return None
def kallein(nimi):
    kallis = db.execute("SELECT MAX(hinta) FROM Tuotteet").fetchone()
    return(kallis)

