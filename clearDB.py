import sqlite3
import ast
from utils import stringParsing




conn = sqlite3.connect("testDB.db")

# SQL table to Python dict
conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

cursor = conn.cursor()

print ("Connected to database successfully")


cursor.execute("""
    DROP TABLE IF EXISTS Events;
""")



cursor.execute("""
    CREATE TABLE Events (
        BeginTime TIME,
        EndTime TIME,
        Location NVARCHAR(50),
        Bio NVARCHAR(500),
        Date DATE,
        Abstract NVARCHAR(500),
        Speaker NVARCHAR(20),
        Host NVARCHAR(20),
        PRIMARY KEY (Location, BeginTime, Date)
    );
""")


# with open("update.txt", "r") as updateFile:
#     fileString = updateFile.read()
#     try:
#         # List of Dicts
#         updateDicts = ast.literal_eval(fileString) # Safe eval() here
#     except:
#         pass
#
#
#
#
# for updateDict in updateDicts:
#     keyString, valueString = stringParsing.rawString2SQL(updateDict)
#
#
#     print(keyString)
#     print(valueString)
#
#
#
#     query = "INSERT INTO Events (%s) VALUES (%s)" % (keyString, valueString)
#
#
#     cursor.execute(query)
#     conn.commit()
cursor.close()
