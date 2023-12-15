from customTypes.weekTimeTypes import *

class Subject:
    name: str
    weight: int

class SubjectsToAllocate:
    totalWeight: int
    subjects: list[Subject]

class StudySession:
    start: weekTime
    end: weekTime
    
class AllocatedStudySession:
    subjectName: str
    subjectSessions: list[StudySession]
