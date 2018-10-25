from urllib import parse
import requests
import json

from urllib.request import urlopen



# The format of the time is like this: 
#   hh:mm-hh:mm, month(full name) day(int)
#   e.g. 14:00—15:00, August 5


department = "GEC"
title = "Lecture A"
host = "ZYF"
speaker = "ZYF"


time = "20:00-21:00, October 19"
location = "Location"
abstract = "Abstract"
bio = "Bio"



data1 = {"Title": title, "Host": host, "Speaker": speaker, "Time": time, "Location": location,\
         "Abstract": abstract, "Bio": bio, "Department": department}



url = 'http://10.15.21.58:80/events/' + department + '?action=add'
requests.post(url, data=json.dumps(data1))
