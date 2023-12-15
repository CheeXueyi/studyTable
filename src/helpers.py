def printCommands() -> None:
    commands = [
        # subject commands
        "as: add subject",
        "es: edit existing subject",
        "ss: show existing subjects",

        # study subject commands
        "ap: add study session",
        "as: edit existing study session",
        "ss: show existing study sessions",

        # timetable
        "p: automatically allocate subjects to study sessions"
        "sp: show timetable"
        
        # others
        "h: show commands"
        "E: exit program"
    ]
    print("Commands:")
    for command in commands:
        print(command)
    