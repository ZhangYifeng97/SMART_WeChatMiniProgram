from urllib import parse
import requests
import json

from urllib.request import urlopen



department = "GEC"
time = "20:00-21:00, October 19"
location = "Location"




data1 = {"Time": time, "Location": location, "Department": department}



url = 'http://10.15.21.58:80/events/' + department + '?action=delete'
requests.post(url, data=json.dumps(data1))
