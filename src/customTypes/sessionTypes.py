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
    
class AllocatedStudySession:
    subjectName: str
    subjectSessions: list[StudySession]
