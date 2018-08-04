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
            PRIMARY KEY (Location, Date, BeginTime)
        );
    """)

    print ("Table created successfully")



    conn.commit()

    conn.close()
