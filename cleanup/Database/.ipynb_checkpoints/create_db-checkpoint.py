#!/usr/bin/env python3
import sqlite3
import os.path
from os import path

def create(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("CREATE TABLE Destination(Name TEXT, Country Text, Description TEXT);")
    c.execute("CREATE TABLE Lodging(Name TEXT, DestinationID INT, Address TEXT, StarRating INT, Description TEXT);")
    c.execute("CREATE TABLE Dining(Name TEXT, DestinationID INT, Address TEXT, CusineType TEXT, RelativeCost TEXT, Description TEXT);")
    c.execute("CREATE TABLE Attractions(Name TEXT, DestinationID INT, Address TEXT, Description TEXT, Cost REAL);")
    conn.commit()
    conn.close()
    
    
if __name__ == '__main__':
    if path.exists("travel_db"):
        print("db already exists")
    else:
        create("travel_db")