import sqlite3
import ast
from . import stringParsing

names = ["GEC", "SIST", "SLST", "SPST", "SEM", "SCA", "IMS", "Favorite"]

posDB = {}
posUpdate = {}
for name in names:
    posDB[name] = "database/"+name+".db"
    posUpdate[name] = "update/"+name+".txt"


def getPopularEvents():
    conn = sqlite3.connect("database/Favorite.db")
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = conn.cursor()
    query = """
            SELECT * FROM (
                SELECT Date, BeginTime, Location, COUNT(*) AS count FROM events
                WHERE (date(Date) >= date('now'))
                GROUP BY Date, BeginTime, Location
                ORDER BY count DESC
            ) LIMIT 10 ;
            """
    cursor.execute(query)
    return cursor.fetchall()




def getUserFavoriteEvents(userID):
    print("events for " + userID)
    conn = sqlite3.connect("database/Favorite.db")
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = conn.cursor()
    query = """
        SELECT * FROM Events AS E
        WHERE (E.userID = \'%s\')
        ORDER BY date(E.Date), time(E.BeginTime) ASC;
        """ % (userID)
    print("executing: " + query)
    cursor.execute(query)
    return cursor.fetchall()



def updateDB(whichDB, postJSON):

    conn = sqlite3.connect(posDB[whichDB])

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    print(postJSON)
    print(type(postJSON))
    updateDict = eval(postJSON)






    keyString, valueString = stringParsing.rawString2SQL(updateDict)


    # REPLACE: UPDATE if EXISTS else INSERT
    query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)


    cursor.execute(query)
    conn.commit()
    cursor.close()






def getDataFromDB(whichDB):

    conn = sqlite3.connect(posDB[whichDB])

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")



    # List of Dicts
    # Stores events for each coming day
    # Index range [0, 13]
    # Today = 0
    # Tomorrow = 1
    # ...
    # Max = 13

    fourteenDaysEvents = []

    # If you are reading this, I'm sorry
    # I don't know how to implement this elegantly

    # Day 0
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 1
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+1 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 2
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+2 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 3
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+3 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 4
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+4 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 5
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+5 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 6
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+6 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 7
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+7 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 8
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+8 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 9
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+9 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 10
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+10 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 11
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+11 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 12
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+12 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 13
    cursor.execute("""
        SELECT * FROM Events AS E
        WHERE (date(E.Date) == date('now', '+13 day'))
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """)
    fourteenDaysEvents.append(cursor.fetchall())

    print(fourteenDaysEvents)
    print(len(fourteenDaysEvents)) # = 14

    return fourteenDaysEvents
