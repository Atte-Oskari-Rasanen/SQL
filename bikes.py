''' 
Tehtäväsi on laatia Pythonilla moduuli bikes.py, joka tarjoaa seuraavat funktiot:

1. distance_of_user(user) ilmoittaa käyttäjän ajaman yhteismatkan. (2 pistettä)

2. speed_of_user(user) ilmoittaa käyttäjän keskinopeuden (km/h) kaikilla matkoilla kahden desimaalin tarkkuudella. (3 pistettä)

3. duration_in_each_city(day) ilmoittaa jokaisesta kaupungista, kauanko pyörillä ajettiin annettuna päivänä. (4 pistettä)

4. users_in_city(city) ilmoittaa, montako eri käyttäjää pyörillä on ollut annetussa kaupungissa. (3 pistettä)

5. trips_on_each_day(city) ilmoittaa jokaisesta päivästä, montako matkaa kyseisenä päivänä on ajettu. (4 pistettä)

6. most_popular_start(city) ilmoittaa kaupungin suosituimman aloitusaseman matkalle sekä matkojen määrän. (4 pistettä)


and we have 
CREATE TABLE Cities (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE Stops (id INTEGER PRIMARY KEY, name TEXT, city_id INTEGER REFERENCES Cities);
CREATE TABLE Bikes (id INTEGER PRIMARY KEY, name TEXT, city_id INTEGER REFERENCES Cities);
CREATE TABLE Trips (id INTEGER PRIMARY KEY, from_id INTEGER REFERENCES Stops, to_id INTEGER REFERENCES Stops, user_id INTEGER REFERENCES Users, bike_id INTEGER REFERENCES Bikes, day TEXT, duration INTEGER, distance INTEGER);

'''
import sqlite3 
db = sqlite3.connect("bikes.db")
db.isolation_level = None

def distance_of_user(user):
    dist = db.execute("select distance from trips where id=?", [user]).fetchone()
    return dist[0]

print(distance_of_user(2))

def speed_of_user(user):
    speed = db.execute("select round((distance/1000.0)/(duration/60.0),2) from trips where id=?;", [user]).fetchone()
    return speed[0]

print(speed_of_user(2))

def duration_in_each_city(day):
    duration = db.execute("select sum(duration) from trips where day=? group by from_id;", [day]).fetchall()
    return duration[0]
print(duration_in_each_city("2021-06-20"))

def users_in_city(city):
    users = db.execute('select count(bike_id) from trips where from_id=?;', [city]).fetchall()
    return users[0]