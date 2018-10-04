import sqlite3
names = ["GEC", "SIST", "SLST", "SPST", "SEM", "SCA", "IMS"]
for name in names:
    conn = sqlite3.connect("database.db")
    print ("Connected to database successfully")

    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS %s;
    """ % name)

    cursor.execute("""
        CREATE TABLE %s (
            Title NVARCHAR(30),
            Host NVARCHAR(30),
            Date DATE,
            BeginTime TIME,
            EndTime TIME,
            Location NVARCHAR(20),
            Bio NVARCHAR(500),
            Speaker NVARCHAR(30),
            Abstract NVARCHAR(500),
            ImageURL NVARCHAR(256),
            PRIMARY KEY (Location, Date, BeginTime)
        );
    """ % name)

    print ("Table created successfully")

    keyString = "Title, Host, Date, BeginTime, EndTime, Location, Bio, Speaker, Abstract, ImageURL"

    valueString = "\'Title\', \'Host\', \'2018-10-07\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-10-08\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-10-09\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-10-10\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-10-11\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-10-12\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (name, keyString, valueString)
    print(query)
    cursor.execute(query)

    conn.commit()

    conn.close()
