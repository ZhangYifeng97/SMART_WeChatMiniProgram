import sqlite3
names = ["GEC", "SIST", "SLST", "SPST", "SEM", "SCA", "IMS"]
for name in names:
    conn = sqlite3.connect("database/%s.db" % name)
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
            ImageURL NVARCHAR(256),
            PRIMARY KEY (Location, Date, BeginTime)
        );
    """)

    print ("Table created successfully")

    keyString = "Title, Host, Date, BeginTime, EndTime, Location, Bio, Speaker, Abstract, ImageURL"

    valueString = "\'Title\', \'Host\', \'2018-08-22\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-08-22\', \'12:00:00\', \'13:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-08-24\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-08-25\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-08-26\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    valueString = "\'Title\', \'Host\', \'2018-08-27\', \'11:00:00\', \'12:00:00\', \'Location\', \'Bio\', \'Speaker\', \'Abstract\', \'ImageURL\'"
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)
    print(query)
    cursor.execute(query)

    conn.commit()

    conn.close()
