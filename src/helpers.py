from customTypes.sessionTypes import Subject
from customTypes.weekTimeTypes import weekTime
from data.datastore import getData

def printCommands() -> None:
    commands = [
        "---Subject commands---",
        "as <subjectName> <weight>: add subject",
        "es <subjectName> <weight>: edit existing subject",
        "ss: show existing subjects",
        "\n",
        "---Study subject commands---",
        "time format: DD:HH:MM, monday is 00, sunday is 06, 24 hour format",
        "ap <starting time> <ending time>: add study session",
        "ep: edit existing study session",
        "sp: show existing study sessions",
        "\n",
        "---Timetable---",
        "p: automatically allocate subjects to study sessions",
        "sp: show timetable",
        "\n",
        "---Others---",
        "s: save data",
        "h: show commands",
        "E: exit program"
    ]
    print("Commands:")
    for command in commands:
        print(command)
    
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
