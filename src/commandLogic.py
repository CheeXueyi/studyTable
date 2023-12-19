import typing
from customTypes.errorTypes import subjectExistsError
from customTypes.sessionTypes import StudySession, Subject
from customTypes.weekTimeTypes import weekTime
from data.datastore import getData
from helpers import findSubjectByName, parseTimeStr, timePeriodsIntersect, timeStrCheck


def addSubjectErrorChecker(name: str, weight: str):
    if weight.isdigit() == False:
        raise TypeError("Weight must be an integer")
    if findSubjectByName(name) != None:
        raise subjectExistsError(f"Subject named {name} already exists")
    if not 0 < len(name) < 20:
        raise Exception("name must be between 1 and 19 characters in length")
        
def addSubject(name: str, weight: str):
    addSubjectErrorChecker(name, weight)

    weightInt = int(weight)
    newSubject = Subject(name, weightInt)
    
    getData().subjects.append(newSubject)

    print(f"Added {name} to subjects with weight {weight}.")

def editSubjectErrorChecker(name: str, weight: str):
    if weight.isdigit() == False:
        raise TypeError("Weight must be an integer")
    if findSubjectByName(name) == None:
        raise Exception(f"Subject named {name} does not exist")

def editSubject(name: str, weight: str):
    editSubjectErrorChecker(name, weight)

    weightInt = int(weight)
    subjectToEdit = typing.cast(Subject, findSubjectByName(name))
    subjectToEdit.weight = weightInt

    print(f"Edited subject {name} to have weight {weight}.")
    
def showSubjects():
    data = getData()
    if len(data.subjects) == 0:
        print("No subjects")
        return
    
    print("Printing subjects")
    lineLength = 38
    print("-"*lineLength)
    print(f" {'index':<6}| {'name':<20}| {'weight':<8}")
    print("-"*lineLength)
    for num, sub in enumerate(data.subjects):
        print(f" {num+1:<6}| {sub.name:<20}| {sub.weight:<8}")
    print("-"*lineLength)

def addPeriodErrorChecker(startTimeRaw: str, endTimeRaw: str):
    if False in [timeStrCheck(startTimeRaw), timeStrCheck(endTimeRaw)]:
        raise Exception("Invalid time inputted")

    startTime = parseTimeStr(startTimeRaw)
    endTime = parseTimeStr(endTimeRaw)
    weekStartTime = weekTime()

    if startTime.timeMinus(weekStartTime).greaterThanEqual(endTime.timeMinus(weekStartTime)):
        raise Exception("starttime must be before endtime in the same week")
    
    # check that this time period does not intersect with another time period
    for p in getData().studySessions:
        if (timePeriodsIntersect(p.start, p.end, startTime, endTime)):
            raise Exception("new studyPeriod cannot intersect with existing studyPeriods")

def addPeriod(startTimeRaw: str, endTimeRaw: str):
    addPeriodErrorChecker(startTimeRaw, endTimeRaw)

    # no error, add study period to database such that study periods are sorted
    # by startTime
    startTime = parseTimeStr(startTimeRaw)
    endTime = parseTimeStr(endTimeRaw)

    studySessions = getData().studySessions
    startOfWeek = weekTime()
    startTimeFromStartOfWeek = startTime.timeMinus(startOfWeek)
    
    # search for insert position and insert
    i = 0
    while (
        i < len(studySessions) and not
        studySessions[i].start.timeMinus(startOfWeek).greaterThan(startTimeFromStartOfWeek)
    ):
        i += 1

    newStudySession = StudySession(startTime, endTime)
    getData().studySessions.insert(i, newStudySession)

    # print success message
    print(f"Added new study session from {startTimeRaw} to {endTimeRaw}.")


def printCommands() -> None:
    commands = [
        "---Subject commands---",
        "as <subjectName> <weight>: add subject",
        "es <subjectName> <weight>: edit existing subject",
        "ss: show existing subjects",
        "\n",
        "---Study session commands---",
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
    

    
    