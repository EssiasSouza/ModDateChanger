import os
from datetime import datetime, timedelta

with open("listToChange.txt", 'r') as listToChange:
    ChangeLines = [linha.strip().split(",") for linha in listToChange]
    for item in ChangeLines:
        objectToChange = item[0]
        newdate = item[1]
        print(f"Object: {objectToChange} - New date: {newdate}") 
        print(newdate)
        modificationSet = newdate
        start_date = datetime.strptime(modificationSet, "%Y-%m-%d")
        print(start_date)
        timestamp = start_date.timestamp()
        os.utime(objectToChange, (timestamp, timestamp))