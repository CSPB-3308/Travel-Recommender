#!/usr/bin/env python3

import os
import sys
import query_db

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print("Usage: load_db_tool.py [-D, -d, -a, -l] [filename]")
        print("-D: Destination File\n -d: Dining File\n -a: Attractions File\n -l: Lodging File")
        
    else:
        fileType = sys.argv[1]
        fileName = sys.argv[2]
        
        file = open(fileName, 'r') 
        lines = file.readlines() 
        
        queryHandler = query_db.QueryHandler()
        
        for line in lines:
            dataFields = line.split()
            
            if fileType == "-a":
                queryHandler.addAttraction(dataFields[0], dataFields[1], dataFields[2], dataFields[3], dataFields[4])
                
            else if fileType == "-d":
                queryHandler.addDining(dataFields[0], dataFields[1], dataFields[2], dataFields[3], dataFields[4], dataFields[5])
    
            else if fileType == "-D":
                queryHandler.addDestination(dataFields[0], dataFields[1], dataFields[2])
            
            else if fileType == "-l"
                queryHandler.addLodging(dataFields[0], dataFields[1], dataFields[2], dataFields[3], dataFields[4])
                
        file.close()
        queryHandler.close_conn()