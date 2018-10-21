import sqlite3


conn = sqlite3.connect("database.db")
print ("Connected to database successfully")

cursor = conn.cursor()




cursor.execute("""
    DROP TABLE IF EXISTS Users;
""")

cursor.execute("""
    CREATE TABLE Users (
        UserID NVARCHAR(30),
        Nickname NVARCHAR(30),
        Gender BINARY,
        City NVARCHAR(10),
        Province NVARCHAR(10),
        Country NVARCHAR(10),
        PRIMARY KEY UserID
    );
""")


keyString = "UserID, Nickname, Gender, City, Province, Country"

valueString = "\'0\', \'aabb\', \'0\', \'Shanghai\', \'Shanghai\', \'China\'"
query = "REPLACE INTO Users (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)
conn.commit()
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

conn.close()