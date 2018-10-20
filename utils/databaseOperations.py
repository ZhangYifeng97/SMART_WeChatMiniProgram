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
                SELECT E.*, COUNT(*) AS count FROM Favorite F
                LEFT JOIN Events E on E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
                WHERE (date(E.Date) >= date(datetime('now', '+8 hours')))
                GROUP BY E.Date, E.BeginTime, E.Location
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
        SELECT E.* FROM Favorite F 
        LEFT JOIN Events E ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) >= date(datetime('now', '+8 hours'))) AND F.UserID = \'%s\'
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        """ % (UserID)


    print("executing: " + query)
    cursor.execute(query)
    return cursor.fetchall()



def replaceIntoDB(postJSON):

    conn = sqlite3.connect(DBLocation)

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    print(postJSON)
    # print(type(postJSON))
    updateDict = postJSON


    keyString, valueString = stringParsing.dict2SQL(updateDict)


    # REPLACE: UPDATE if EXISTS else INSERT
    query = "REPLACE INTO %s (%s) VALUES (%s)" % (tableName, keyString, valueString)


    cursor.execute(query)
    conn.commit()
    cursor.close()



def deleteFromDB(postJSON):

    conn = sqlite3.connect(DBLocation)

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    print(postJSON)

    updateDict = postJSON



    # keyString, valueString = stringParsing.dict2SQL(updateDict)

    # print(keyString, valueString)


    # keys = keyString.split(",")
    # values = valueString.split(",")
    conditions = ["%s = \'%s\'" % (key, updateDict[key]) for key in updateDict]
    conditionString = " AND ".join(conditions)



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
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 1
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+1 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 2
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+2 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 3
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+3 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 4
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+4 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 5
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+5 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 6
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+6 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 7
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+7 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 8
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+8 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 9
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+9 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 10
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+10 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 11
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+11 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 12
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+12 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    # Day 13
    cursor.execute("""
        SELECT E.*, COUNT(DISTINCT F.UserID) AS 'Counter'
        FROM Events E LEFT JOIN Favorite F ON E.Date = F.Date AND E.BeginTime = F.BeginTime AND E.Location = F.Location AND E.Department = F.Department
        WHERE (date(E.Date) == date(datetime('now', '+13 day', '+8 hours'))) AND E.Department = \'%s\'
        GROUP BY E.Date, E.BeginTime, E.Location
        ORDER BY date(E.Date), time(E.BeginTime) ASC
        ;
    """ % departmentName)
    fourteenDaysEvents.append(cursor.fetchall())

    print(fourteenDaysEvents)
    print(len(fourteenDaysEvents)) # = 14

    return fourteenDaysEvents
