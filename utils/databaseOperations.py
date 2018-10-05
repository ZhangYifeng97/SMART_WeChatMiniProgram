import sqlite3
import ast
from . import stringParsing

DBLocation = "database.db"

def getPopularEvents():
    conn = sqlite3.connect(DBLocation)
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = conn.cursor()
    query = """
            SELECT * FROM (
                SELECT Date, BeginTime, Location, COUNT(*) AS count FROM Favorite
                WHERE (date(Date) >= date('now'))
                GROUP BY Date, BeginTime, Location
                ORDER BY count DESC
            ) LIMIT 10 ;
            """
    cursor.execute(query)
    return cursor.fetchall()




def getUserFavoriteEvents(UserID):
    print("events for " + UserID)
    conn = sqlite3.connect(DBLocation)
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = conn.cursor()
    query = """
        SELECT * FROM Favorite AS E
        WHERE (E.UserID = \'%s\')
        ORDER BY date(E.Date), time(E.BeginTime) ASC;
        """ % (UserID)
    print("executing: " + query)
    cursor.execute(query)
    return cursor.fetchall()



def replaceIntoDB(tableName, postJSON):

    conn = sqlite3.connect(DBLocation)

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    print(postJSON)
    print(type(postJSON))
    updateDict = eval(postJSON)

    keyString, valueString = stringParsing.dict2SQL(updateDict)


    # REPLACE: UPDATE if EXISTS else INSERT
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (tableName, keyString, valueString)


    cursor.execute(query)
    conn.commit()
    cursor.close()



def deleteFromDB(tableName, postJSON):

    conn = sqlite3.connect(DBLocation)

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    print(postJSON)
    print(type(postJSON))
    updateDict = eval(postJSON)



    keyString, valueString = stringParsing.dict2SQL(updateDict)

    keys = keyString.split(",")
    values = valueString.split(",")
    conditions = ["%s = %s" % (i, j) for i, j in zip(keys, values)]
    conditionString = " AND".join(conditions)



    query = "DELETE FROM %s WHERE %s;" % (tableName, conditionString)
    print(query)


    cursor.execute(query)
    conn.commit()
    cursor.close()


def getFourteenDaysEvents(departmentName):

    conn = sqlite3.connect(DBLocation)

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
    # I don't know how to implement with elegance

    # Day 0
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 1
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+1 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 2
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+2 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 3
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+3 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 4
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+4 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 5
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+5 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 6
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+6 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 7
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+7 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 8
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+8 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 9
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+9 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 10
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+10 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 11
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+11 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 12
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+12 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 13
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM %s E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location
        WHERE (date(E.Date) == date('now', '+13 day'))
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    print(fourteenDaysEvents)
    print(len(fourteenDaysEvents)) # = 14

    return fourteenDaysEvents
