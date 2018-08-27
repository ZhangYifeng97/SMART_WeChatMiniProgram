import sqlite3


conn = sqlite3.connect("database/Favorite.db")
print ("Connected to database successfully")

cursor = conn.cursor()




cursor.execute("""
    DROP TABLE IF EXISTS Events;
""")

cursor.execute("""
    CREATE TABLE Events (
        Date DATE,
        BeginTime TIME,
        Location NVARCHAR(20),
        userID NVARCHAR(32),
        PRIMARY KEY (Location, Date, BeginTime, userID)
    );
""")


keyString = "Date, BeginTime, Location, userID"

valueString = "\'2018-08-22\', \'11:00:00\', \'SIST\', \'lsd\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)


valueString = "\'2018-08-22\', \'11:00:00\', \'SIST\', \'zyf\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-08-22\', \'11:00:00\', \'SIST\', \'sy\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-08-22\', \'12:00:00\', \'SIST\', \'zyf\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-08-22\', \'12:00:00\', \'SIST\', \'lsd\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-08-22\', \'13:00:00\', \'SIST\', \'zyf\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'2018-08-22\', \'14:00:00\', \'SIST\', \'zyf\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)
conn.commit()

cursor.execute("SELECT * FROM Events")
print(cursor.fetchall())

conn.close()
