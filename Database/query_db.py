#!/usr/bin/env python3
import sqlite3
from enum import Enum

class Error(Enum):
    Success = 0
    SQLExecuteError = 1
    ValueErr = 3
    InvalidDest = 4
    InvalidQuery = 5
    
class QueryHandler:
    def __init__(self):
        db_name = "travel_db"
        conn = sqlite3.connect(dbName)
        c = conn.cursor()

    def close_conn(self):
        self.conn.close()

    def addDestination(self, name, country, descr):

        if type(name) != str or type(descr) != str or type(productName) != str:
            return Error.ValueErr
        try: 
            self.c.execute("INSERT INTO Destination VALUES(?, ?, ?);", (name, country, descr))
            self.conn.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
        
    def addLodging(self, name, destName, address, starRating, descr):
        
        if type(name) != str or type(descr) != str or type(destName) != str or type(starRating) != str or type(address) != str:
            return Error.ValueErr
        
        # make sure destination exists in dB and pull its row id
        c.execute("SELECT rowid FROM Destination WHERE Name=" + str(destName) + ";")
    
        row = c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Lodging VALUES(?, ?, ?, ?, ?);", (name, destID, address, starRating, descr))
            self.c.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    def addDining(self, name, destName, address, cuisineType, relCost, descr):
         
        if type(name) != str or type(descr) != str or type(destName) != str or type(relCost) != str or type(address) != str or type(cuisineType) != str:
            return Error.ValueErr
        
        # make sure destination exists in dB and pull its row id
        c.execute("SELECT rowid FROM Destination WHERE Name=" + str(destName) + ";")
    
        row = c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Dining VALUES(?, ?, ?, ?, ?, ?);", (name, destID, address, cuisineType, relCost, descr))
            self.c.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    def addAttraction(self, name, destName, address, descr, cost):
        
        if type(name) != str or type(descr) != str or type(destName) != str or type(cost) != float or type(address) != str:
            return Error.ValueErr
        
        # make sure destination exists in dB and pull its row id
        c.execute("SELECT rowid FROM Destination WHERE Name=" + str(destName) + ";")
    
        row = c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Attractions VALUES(?, ?, ?, ?, ?);", (name, destID, address, cost, descr))
            self.c.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    
    def queryRecommendations(self, destination, requestType):
        # Queries DB based on destination and request
        # requestType must be Attractions, Dining, or lodging
        if requestType not in ["Attractions", "Dining", "Lodging"]:
            return Error.InvalidQuery
        
        try:
            c.execute("SELECT rowid FROM Destination WHERE Name=" + str(destination) + ";")
            destRow = c.fetchone()
            if destRow is None;
                return None
            
            self.c.execute("SELECT * FROM " + requestType + "WHERE DestinationID=" + str(destID) + ";")
            
            return self.c.fetchall()
        
        except:
            return Error.SQLExecuteError