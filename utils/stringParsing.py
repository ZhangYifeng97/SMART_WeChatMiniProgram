def monthString2Num(string):
    print("monthString: ", string)
    m = {
            'jan': "01",
            'feb': "02",
            'mar': "03",
            'apr': "04",
            'may': "05",
            'jun': "06",
            'jul': "07",
            'aug': "08",
            'sep': "09",
            'oct': "10",
            'nov': "11",
            'dec': "12"
        }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        print(s)
        raise ValueError('Not a month')



def userInfo2SQL(userInfo):
    postJSON = {}
    postJSON["UserID"] = userInfo["OpenId"]
    postJSON["Nickname"] = userInfo["nickName"]
    postJSON["Gender"] = userInfo["gender"]
    postJSON["City"] = userInfo["city"]
    postJSON["Province"] = userInfo["province"]
    postJSON["Country"] = userInfo["country"]
    return postJSON

def dict2SQL(updateDict):
    from datetime import datetime
    import re

    # Raw dict, for adding events into table
    if "Time" in [key for key in updateDict]:
        keys = [key for key in updateDict if key != "Time"]
        values = ["\'" + updateDict[key].replace("\'", "\'\'") + "\'" for key in keys]
        keys.append("BeginTime")
        keys.append("EndTime")
        keys.append("Date")
        originalTimeString = updateDict["Time"]
        print("originalTimeString:", originalTimeString)

        replaceTimeString = originalTimeString.replace("—", " ").replace(",", "").replace("-", " ")
        print("replaceTimeString:", replaceTimeString)

        splitTimeList = [x for x in replaceTimeString.split(" ") if x]

        print("splitTimeList:", splitTimeList)
        startHourString = splitTimeList[0]
        endHourString = splitTimeList[1]
        monthNameString = splitTimeList[2]
        monthNumString = monthString2Num(splitTimeList[2])
        dayNumString = "%02d" % int(splitTimeList[3])


        if datetime.now().month > int(monthNumString):
            date = "\'" + str(datetime.now().year + 1) + "-" + monthNumString + "-" + dayNumString + "\'"
        else:
            date = "\'" + str(datetime.now().year) + "-" + monthNumString + "-" + dayNumString + "\'"

        BeginTime = "\'" + startHourString + ":00\'"

        EndTime = "\'" + endHourString + ":00\'"

        values.append(BeginTime)
        values.append(EndTime)
        values.append(date)
        keyString = ", ".join(keys)
        valueString = ", ".join(values)


    # Dict after modification by previous steps
    else:
        keys = [key for key in updateDict]
        values = ["\'" + updateDict[key].replace("\'", "\'\'") + "\'" for key in keys]


    keyString = ", ".join(keys)
    valueString = ", ".join(values)
    return keyString, valueString
