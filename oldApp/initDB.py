import sqlite3
names = ["GEC", "SIST", "SLST", "SPST", "SEM", "SCA", "IMS"]
for name in names:
    conn = sqlite3.connect("db/%s.db" % name)
    print ("Connected to database successfully")

    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS Events;
    """)

    cursor.execute("""
        CREATE TABLE Events (
            Name NVARCHAR(30),
            Date DATE,
            BeginTime TIME,
            EndTime TIME,
            Location NVARCHAR(20),
            Description NVARCHAR(500),
            PRIMARY KEY (Location, Date, BeginTime)
        );
    """)

    print ("Table created successfully")

    cursor.execute("""
        INSERT INTO Events (Name, Date, BeginTime, EndTime, Location, Description)
        VALUES
        ('吐槽操作系统', '2018-07-21', '19:00:00', '20:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐吐槽吐槽'),
        ('吐槽操作系统', '2018-07-21', '13:00:00', '14:00:00', 'SIST 1D-301', '吐   槽吐槽吐槽
    吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-21', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-23', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-20', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-22', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-09-19', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-08-01', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-19', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽'),
        ('吐槽操作系统', '2018-07-24', '10:00:00', '12:00:00', 'SIST 1D-301', '吐槽吐槽吐槽吐槽吐槽吐槽吐槽吐槽')
        ;
    """)


    conn.commit()

    conn.close()
