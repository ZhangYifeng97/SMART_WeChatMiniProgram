import sqlite3


conn = sqlite3.connect("database.db")
print ("Connected to database successfully")

cursor = conn.cursor()




cursor.execute("""
    DROP TABLE IF EXISTS Favorite;
""")

cursor.execute("""
    CREATE TABLE Favorite (
        Date DATE,
        BeginTime TIME,
        Location NVARCHAR(20),
        UserID NVARCHAR(32),
        PRIMARY KEY (Location, Date, BeginTime, UserID)
    );
""")


keyString = "Date, BeginTime, Location, UserID"

valueString = "\'2018-10-12\', \'11:00:00\', \'Location\', \'lsd\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-12\', \'11:00:00\', \'Location\', \'oKhQc5GXLMDiAj7A6urlC60wHaKk\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-12\', \'11:00:00\', \'Location\', \'sy\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-09\', \'11:00:00\', \'Location\', \'oKhQc5GXLMDiAj7A6urlC60wHaKk\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-09\', \'11:00:00\', \'Location\', \'lsd\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-11\', \'11:00:00\', \'Location\', \'oKhQc5GXLMDiAj7A6urlC60wHaKk\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


conn.commit()

cursor.execute("SELECT * FROM Favorite")
print(cursor.fetchall())

conn.close()
