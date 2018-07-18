from flask import Flask
from flask_restful import Api, Resource
import sqlite3
import json


# This HAS to be False if we are actually running it instead of testing it
debugBool = False

app = Flask(__name__)
api = Api(app)


conn = sqlite3.connect("SISTEvents.db")

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

# The ugly part is over



print(fourteenDaysEvents)
print(len(fourteenDaysEvents)) # = 14

class DayEvents(Resource):
    def get(self, day):
        return fourteenDaysEvents[int(day)]


class AllEvents(Resource):
    def get(self):
        return fourteenDaysEvents



## Set up the API route
api.add_resource(AllEvents, '/events')
api.add_resource(DayEvents, '/events/<day>')


if __name__ == '__main__':
    app.run(debug=debugBool)
