from customTypes.sessionTypes import AllocatedStudySession, StudySession, Subject

class DataStore:
    # list of subjects
    subjects: list[Subject] = []
    
    # studySession stuff
    # study sessions in ascending order of time of week
    studySessions: list[StudySession] = []
    totalStudyTime: int = 0

    # allocated study session if it exists
    allocatedStudySession: list[AllocatedStudySession] | None = None

    def __str__(self):
        subjectStrs = []
        for sub in self.subjects:
            subjectStrs.append(f"{sub.name}, {sub.weight}")

        studySessionStrs = []
        for sess in self.studySessions:
            studySessionStrs.append(
                f"day {sess.start.dayNum} {sess.start.hour}:{sess.start.minute} to day {sess.end.dayNum} {sess.end.hour}:{sess.end.minute}"
            )
        
        return f'''subjects: {subjectStrs}
studySessions: {studySessionStrs}
totalStudyTime: {self.totalStudyTime}
allocatedStudySession: {self.allocatedStudySession}
        ''' 

data = DataStore()

def clear() -> None:
    '''
    resets dataStore to blank state
    '''
    global data
    data.subjects = []
    data.studySessions = []
    data.totalStudyTime = 0
    data.allocatedStudySession = None

def getData() -> DataStore:
    '''
    returns the current data
    '''
    global data
    return data

