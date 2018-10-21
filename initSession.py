from sqlitedict import SqliteDict
mydict = SqliteDict('kv.db', autocommit=True)
mydict['some_key'] = ("session_key", "open_id")
print (mydict['some_key'])  # prints the new value
for key in mydict:
    print(key, mydict[key])
print(len(mydict))
mydict.close()
