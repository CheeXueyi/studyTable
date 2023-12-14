from weekTimeTypes import weekTime

class Subject:
    name: str
    weight: int

class SubjectsToAllocate:
    totalWeight: int
    totalHours: int
    subjects: list[Subject]

class StudySession:
    start: weekTime
    end: weekTime
    
class AllocatedStudySession:
    subjectName: str
    subjectSessions: list[StudySession]

class AllocatedStudySessions:
    sessions: list[AllocatedStudySession]
