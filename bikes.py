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
import re
import os
os. getcwd()
path = "/home/atte/Documents/SQL_course" 
os.chdir(path)

db = sqlite3.connect("bikes.db")
db.isolation_level = None

def distance_of_user(user):
    #dist = db.execute("select distance from trips where user_id=?", [user]).fetchone()
    dist = db.execute("select sum(t.distance) from trips t, users u where u.name=? and user_id=u.id;", [user]).fetchone()
    return dist

print(distance_of_user("user123"))

def speed_of_user(user):
#    speed = db.execute("select round((distance/1000.0)/(duration/60.0),2) from trips where id=?;", [user]).fetchone()
    speed = db.execute("select round((sum(distance)/1000.0)/(sum(duration)/60.0),2) from trips t, users u where u.name=? and user_id=u.id;", [user]).fetchone()
    return speed[0]

print(speed_of_user("user123"))

def duration_in_each_city(day):
    #duration = db.execute("select distinct c.name, sum(duration) from trips t, cities c where c.id=t.to_id and t.day=? group by c.name;", [day]).fetchall()
    duration = db.execute('select distinct c.name, sum(duration) from trips t, cities c, stops s where s.city_id=t.from_id and t.day=? group by s.name'[day]).fetchone
    return duration[0]
print(duration_in_each_city("2021-06-20"))

def users_in_city(city):
    #users = db.execute('select count(bike_id) from trips where from_id=?;', [city]).fetchall()
    #users = db.execute('select distinct count(u.id) from trips t, users u, cities c where u.id=t.user_id and c.name=? and t.to_id=c.id;', [city]).fetchall()
    users = db.execute('select count (distinct t.user_id) from trips t, stops s, cities c where s.city_id=t.from_id and c.name=?;', [city]).fetchone()
    #print(users)
    print(users)
    return users[0]
print(duration_in_each_city("city4"))

users = db.execute('select count (distinct t.user_id) from trips t, stops s where s.city_id=t.from_id and cities.name =?;', ['city5']).fetchone()
users[0]
