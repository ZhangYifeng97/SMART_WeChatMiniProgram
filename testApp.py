from flask import Flask
from flask_restful import Api, Resource
import sqlite3
import json
import ast
from utils import stringParsing


############################################################################
# This HAS to be False if we are actually running it instead of testing it #
############################################################################
debugBool = False

app = Flask(__name__)
api = Api(app)




def updateDB():

    conn = sqlite3.connect("testDB.db")

    # SQL table to Python dict
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

    cursor = conn.cursor()

    print ("Connected to database successfully")

    with open("update.txt", "r") as updateFile:
        fileString = updateFile.read()
        try:
            # List of Dicts
            updateDicts = ast.literal_eval(fileString) # Safe eval() here
        except:
            return


    # Clear the file
    with open("update.txt", "w"):
        pass



    for updateDict in updateDicts:
        keyString, valueString = stringParsing.rawString2SQL(updateDict)


        # REPLACE: UPDATE if EXISTS else INSERT
        query = "REPLACE INTO Events (%s) VALUES (%s)" % (keyString, valueString)


        cursor.execute(query)
        conn.commit()
    cursor.close()



def getDataFromDB():

    conn = sqlite3.connect("testDB.db")

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


class SISTEvents(Resource):
    def get(self):
        updateDB()
        return getDataFromDB()

    def put(self):
        # Need a textbox here
        pass

    def delete(self):
        # Need a textbox here
        pass







api.add_resource(SISTEvents, '/events/SIST')


# class DayEvents(Resource):
#     def get(self, day):
#         return getDataFromDB("SIST")[int(day)]
#
#
# class AllEvents(Resource):
#     def get(self):
#         return getDataFromDB("SIST")
#
#
#
# ## Set up the API route
# api.add_resource(AllEvents, '/events')
# api.add_resource(DayEvents, '/events/<day>')


if __name__ == '__main__':
    app.run(debug=debugBool)
