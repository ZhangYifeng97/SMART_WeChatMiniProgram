from urllib import parse
import requests
import json

from urllib.request import urlopen

password = input("Password：")
title = input("Title/标题：")
host = input("Host/主办人（选填）：")
speaker = input("Speaker/主讲人:")
print("The format of the time is like this: 14:00—15:00, August 5(hh:mm-hh:mm, month(full name) day(int)")
time = input("Time/时间：")
location = input("Location/地点：")
abstract = input("Abstract/简介：")
bio = input("Bio/学者简介：")
data2 = {"Password": password}
data1 = {"Title": title, "Host": host, "Speaker": speaker, "Time": time, "Location": location,\
         "Abstract": abstract, "Bio": bio}
data = parse.urlencode(data2).encode('utf-8')
url = 'http://10.15.21.58:80/events/SIST?password='+password
requests.post(url, data=json.dumps(data1))






