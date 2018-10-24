from urllib import parse
import requests
import json

from urllib.request import urlopen


# title = input("Title/标题：")
# host = input("Host/主办人（选填）：")
# speaker = input("Speaker/主讲人:")
# print("The format of the time is like this: 14:00—15:00, August 5(hh:mm-hh:mm, month(full name) day(int)")
# time = input("Time/时间：")
# location = input("Location/地点：")
# abstract = input("Abstract/简介：")
# bio = input("Bio/学者简介：")

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



url = 'http://10.15.21.58:80/events/' + department
requests.post(url, data=json.dumps(data1))
