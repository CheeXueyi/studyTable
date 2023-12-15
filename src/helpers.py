from customTypes.sessionTypes import Subject
from data.datastore import getData

def printCommands() -> None:
    commands = [
        "---Subject commands---",
        "as <subjectName> <weight>: add subject",
        "es <subjectName> <weight>: edit existing subject",
        "ss: show existing subjects",
        "\n",
        "---Study subject commands---",
        "ap: add study session",
        "as: edit existing study session",
        "ss: show existing study sessions",
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
    
def findSubjectByName(name: str) -> Subject | None:
    data = getData()
    for i in data.subjects:
        if i.name == name: return i
    
    return None