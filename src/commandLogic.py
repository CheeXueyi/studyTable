import typing
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
    
