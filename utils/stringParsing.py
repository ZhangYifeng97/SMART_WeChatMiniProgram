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



def rawString2SQL(updateDict):
    from datetime import datetime
    import re
    keys = [key for key in updateDict if key != "Time"]
    values = ["\'" + updateDict[key].replace("\'", "\'\'") + "\'" for key in keys]
    keys.append("BeginTime")
    keys.append("EndTime")
    keys.append("Date")
    originalTimeString = updateDict["Time"]
    print("originalTimeString:", originalTimeString)

    replaceTimeString = originalTimeString.replace("—", " ").replace(",", "").replace("-", " ")
    replaceTimeString = re.sub(' +', ' ', replaceTimeString)
    print("replaceTimeString:", replaceTimeString)

    splitTimeList = replaceTimeString.split(" ")

    print("splitTimeList:", splitTimeList)
    startHourString = splitTimeList[0]
    endHourString = splitTimeList[1]
    monthNameString = splitTimeList[2]
    monthNumString = monthString2Num(splitTimeList[2])
    dayNumString = "%02d" % int(splitTimeList[3])
    date = "\'" + str(datetime.now().year) + "-" + monthNumString + "-" + dayNumString + "\'"

    BeginTime = "\'" + startHourString + ":00\'"

    EndTime = "\'" + endHourString + ":00\'"

    values.append(BeginTime)
    values.append(EndTime)
    values.append(date)
    keyString = ", ".join(keys)
    valueString = ", ".join(values)


    return keyString, valueString
