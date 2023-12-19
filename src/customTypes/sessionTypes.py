from __future__ import annotations
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

    def equal(self, otherSession: StudySession):
        return self.start.equal(otherSession.start) and self.end.equal(otherSession.end)
    
    def __str__(self):
        dayArr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        startTimePretty = f"{str(self.start.hour).zfill(2)}:{str(self.start.minute).zfill(2)}"
        endTimePretty = f"{str(self.end.hour).zfill(2)}:{str(self.end.minute).zfill(2)}"
        return f"{dayArr[self.start.dayNum]} {startTimePretty} - {endTimePretty}"
    
class AllocatedStudySession:
    subjectName: str
    subjectSessions: list[StudySession]
