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
        Department NVARCHAR(4),
        PRIMARY KEY (Location, Date, BeginTime, UserID, Department)
    );
""")


keyString = "Date, BeginTime, Location, UserID, Department"

valueString = "\'2018-10-27\', \'11:00:00\', \'SIST\', \'lsd\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'SIST\', \'zyf\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'SIST\', \'sy\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'SIST\', \'zyf\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SIST\', \'lsd\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SIST\', \'zyf\', \'SIST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'2018-10-27\', \'11:00:00\', \'GEC\', \'lsd\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'GEC\', \'zyf\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'GEC\', \'sy\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'GEC\', \'zyf\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'GEC\', \'lsd\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'GEC\', \'zyf\', \'GEC\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)













valueString = "\'2018-10-27\', \'11:00:00\', \'IMS\', \'lsd\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'IMS\', \'zyf\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'IMS\', \'sy\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'IMS\', \'zyf\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'IMS\', \'lsd\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'IMS\', \'zyf\', \'IMS\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


















valueString = "\'2018-10-27\', \'11:00:00\', \'SCA\', \'lsd\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'SCA\', \'zyf\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'SCA\', \'sy\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'SCA\', \'zyf\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SCA\', \'lsd\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SCA\', \'zyf\', \'SCA\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)















valueString = "\'2018-10-27\', \'11:00:00\', \'SLST\', \'lsd\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'SLST\', \'zyf\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'SLST\', \'sy\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'SLST\', \'zyf\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SLST\', \'lsd\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SLST\', \'zyf\', \'SLST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)







valueString = "\'2018-10-27\', \'11:00:00\', \'SPST\', \'lsd\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'SPST\', \'zyf\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'SPST\', \'sy\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'SPST\', \'zyf\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SPST\', \'lsd\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SPST\', \'zyf\', \'SPST\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)






valueString = "\'2018-10-27\', \'11:00:00\', \'SEM\', \'lsd\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-10-28\', \'11:00:00\', \'SEM\', \'zyf\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-29\', \'11:00:00\', \'SEM\', \'sy\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-30\', \'11:00:00\', \'SEM\', \'zyf\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SEM\', \'lsd\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-10-31\', \'11:00:00\', \'SEM\', \'zyf\', \'SEM\'"
query = "REPLACE INTO Favorite (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)












conn.commit()

cursor.execute("SELECT * FROM Favorite")
print(cursor.fetchall())

conn.close()
