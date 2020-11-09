#!/usr/bin/env python3
import sqlite3
import pdb
from enum import Enum

class Error(Enum):
    Success = 0
    SQLExecuteError = 1
    ValueErr = 3
    InvalidDest = 4
    InvalidQuery = 5
    
class QueryHandler:
    db_name = "db.sqlite3"
    conn = sqlite3.connect(db_name, check_same_thread=False)
    c = conn.cursor()
    
    def close_conn(self):
        self.conn.close()

    def addDestination(self, name, country, descr):

        if type(name) != str or type(descr) != str or type(country) != str:
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
        self.c.execute('SELECT rowid FROM Destination WHERE Name="' + destName + '";')
    
        row = self.c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Lodging VALUES(?, ?, ?, ?, ?);", (name, destID, address, starRating, descr))
            self.conn.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    def addDining(self, name, destName, address, cuisineType, relCost, descr):
         
        if type(name) != str or type(descr) != str or type(destName) != str or type(relCost) != str or type(address) != str or type(cuisineType) != str:
            return Error.ValueErr
        
        # make sure destination exists in dB and pull its row id
        self.c.execute('SELECT rowid FROM Destination WHERE Name="' + destName + '";')
    
        row = self.c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Dining VALUES(?, ?, ?, ?, ?, ?);", (name, destID, address, cuisineType, relCost, descr))
            self.conn.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    def addAttraction(self, name, destName, address, descr, cost):
        
        if type(name) != str or type(descr) != str or type(destName) != str or type(cost) != float or type(address) != str:
            return Error.ValueErr
        
        # make sure destination exists in dB and pull its row id
        self.c.execute('SELECT rowid FROM Destination WHERE Name="' + destName + '";')
    
        row = self.c.fetchone()

        if row is None:
            return Error.InvalidDest
        else:
            destID = row[0]
        
        try:
            self.c.execute("INSERT INTO Attractions VALUES(?, ?, ?, ?, ?);", (name, destID, address, descr, cost))
            self.conn.commit()
        except:
            return Error.SQLExecuteError
        
        return Error.Success
    
    
    def queryRecommendations(self, destination, requestType):
        # Queries DB based on destination and request
        # requestType must be Attractions, Dining, or lodging

        if requestType not in ["attractions", "dining", "lodging", "destination"]:
            return Error.InvalidQuery
        
        try:
            self.c.execute('SELECT rowid FROM destinations_destination WHERE Name="' + destination + '"' + ";")
            destRow = self.c.fetchone()
            if destRow is None:
                return None
            else:
                destID = destRow[0]
            if requestType == "destination":
                self.c.execute("SELECT * FROM destinations_" + requestType + " WHERE rowid=" + str(destID) + ";")
                return self.c.fetchone()
            else: 
                self.c.execute("SELECT * FROM destinations_" + requestType + " WHERE DestinationID=" + str(destID) + ";")
                return self.c.fetchall()
        
        except:
            return Error.SQLExecuteError