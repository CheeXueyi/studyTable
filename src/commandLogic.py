import typing
from customTypes.errorTypes import subjectExistsError
from customTypes.sessionTypes import Subject
from customTypes.weekTimeTypes import weekTime
from data.datastore import getData
from helpers import findSubjectByName, parseTimeStr, timeStrCheck


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

    if not (startTime.timeMinus(weekStartTime).greaterThan(endTime.timeMinus(weekStartTime))):
        raise Exception("starttime must be before endtime in the same week")
    

def addPeriod(startTimeRaw: str, endTimeRaw: str):
    addPeriodErrorChecker(startTimeRaw, endTimeRaw)