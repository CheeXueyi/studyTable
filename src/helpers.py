from customTypes.sessionTypes import Subject
from customTypes.weekTimeTypes import weekTime
from data.datastore import getData

def findSubjectByName(name: str) -> Subject | None:
    data = getData()
    for i in data.subjects:
        if i.name == name: return i
    
    return None

def timeStrCheck(rawTimeStr: str) -> bool:
    '''
    returns true if timeStr is valid. returns false otherwise
    '''
    # check form
    if len(rawTimeStr) != 8: 
        return False
    if rawTimeStr[2] + rawTimeStr[5] != "::":
        return False
    
    dayNumStr = rawTimeStr[0:2]
    hourStr = rawTimeStr[3:5]
    minStr = rawTimeStr[6:8]
    if not (dayNumStr.isdigit() and hourStr.isdigit() and minStr.isdigit()):
        return False
    
    # check valid time numbers
    if not 0 <= int(dayNumStr) <= 6:
        return False
    if not 0 <= int(hourStr) <= 23:
        return False
    if not 0 <= int(minStr) <= 59:
        return False
    
    return True
             
def parseTimeStr(rawTimeStr: str) -> weekTime:
    '''
    Parse a rawTimeStr into a weekTime object. Assumes that rawTimeStr is of 
    valid form.
    '''
    dayNum = int(rawTimeStr[0:2])
    hour = int(rawTimeStr[3:5])
    minute = int(rawTimeStr[6:8])
    return weekTime(dayNum, hour, minute)

def timePeriodsIntersect(
    periodStart1: weekTime, periodEnd1: weekTime,
    periodStart2: weekTime, periodEnd2: weekTime
):
    '''
    Checks if two time periods intersect. Returns false if 2 periods only share
    an end point (ie, 1:00 - 2:00 does not intersect with 2:00 - 3:00)
    '''
    if periodStart1.equal(periodEnd2) or periodStart2.equal(periodEnd1):
        return False
    
    periodCheckers = [
        periodEnd1.timeMinus(periodStart1).greaterThanEqual(periodEnd1.timeMinus(periodStart2)),
        periodEnd2.timeMinus(periodStart2).greaterThanEqual(periodEnd2.timeMinus(periodStart1))
    ]
    
    if True in periodCheckers:
        return True
    else:
        return False
    
    