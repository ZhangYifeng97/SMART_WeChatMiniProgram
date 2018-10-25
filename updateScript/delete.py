from urllib import parse
import requests
import json

from urllib.request import urlopen



department = "GEC"
begintime = "20:00:00"
date = "2018-10-19"
location = "Location"




data1 = {"BeginTime": begintime, "Location": location, "Department": department}



url = 'http://10.15.21.58:80/events/' + department + '?action=delete'
requests.post(url, data=json.dumps(data1))
