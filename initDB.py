import sqlite3


conn = sqlite3.connect("database.db")
print ("Connected to database successfully")

cursor = conn.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS Events;
""")

cursor.execute("""
    CREATE TABLE Events (
        Title NVARCHAR(30),
        Host NVARCHAR(30),
        Date DATE,
        BeginTime TIME,
        EndTime TIME,
        Location NVARCHAR(20),
        Bio NVARCHAR(500),
        Speaker NVARCHAR(30),
        Abstract NVARCHAR(500),
        Department NVARCHAR(4),
        PRIMARY KEY (Location, Date, BeginTime, Department)
    );
""")

print ("Table created successfully")

keyString = "Title, Host, Date, BeginTime, EndTime, Location, Bio, Speaker, Abstract, Department"

valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'SIST\', \'Bio\', \'Speaker\', \'Abstract\', \'SIST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'GEC\', \'Bio\', \'Speaker\', \'Abstract\', \'GEC\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'IMS\', \'Bio\', \'Speaker\', \'Abstract\', \'IMS\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'SPST\', \'Bio\', \'Speaker\', \'Abstract\', \'SPST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)



valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'SLST\', \'Bio\', \'Speaker\', \'Abstract\', \'SLST\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'SEM\', \'Bio\', \'Speaker\', \'Abstract\', \'SEM\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)




valueString = "\'Title\', \'Host\', \'2018-10-27\', \'11:00:00\', \'12:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-28\', \'11:00:00\', \'12:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-29\', \'11:00:00\', \'12:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-30\', \'11:00:00\', \'12:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'11:00:00\', \'12:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)

valueString = "\'Title\', \'Host\', \'2018-10-31\', \'12:00:00\', \'13:00:00\', \'SCA\', \'Bio\', \'Speaker\', \'Abstract\', \'SCA\'"
query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
print(query)
cursor.execute(query)



conn.commit()

conn.close()
