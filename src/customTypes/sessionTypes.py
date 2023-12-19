from customTypes.weekTimeTypes import *

class Subject:        
    name: str
    weight: int

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class SubjectsToAllocate:
    totalWeight: int
    subjects: list[Subject]

class StudySession:
    start: weekTime
    end: weekTime

    def __init__(self, start: weekTime, end: weekTime):
        self.start = start
        self.end = end
    
class AllocatedStudySession:
    subjectName: str
    subjectSessions: list[StudySession]
