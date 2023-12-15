from customTypes.errorTypes import subjectExistsError
from customTypes.sessionTypes import Subject
from data.datastore import getData
from helpers import findSubjectByName


def addSubjectErrorChecker(name: str, weight: str):
    if weight.isdigit() == False:
        raise TypeError("Weight must be an integer")
    if findSubjectByName(name) != None:
        raise subjectExistsError(f"Subject named {name} already exists")
        
def addSubject(name: str, weight: str):
    addSubjectErrorChecker(name, weight)

    data = getData()

    weightInt = int(weight)

    newSubject = Subject(name, weightInt)
    data.subjects.append(newSubject)
    print(f"Added {name} to subjects with weight {weight}.")