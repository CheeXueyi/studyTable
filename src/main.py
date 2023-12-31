from commandLogic import addPeriod, addSubject, deletePeriod, editSubject, showPeriods, showSubjects, printCommands
from data.datastore import getData, clear

# main loop
printCommands()
while(True):
    command = input("\nCommand: ")
    match command.split():
        # ---------- subject commands ----------
        case ["as", *args]:
            if (len(args) != 2): 
                print("incorrect number of arguments")
                continue
            try:
                addSubject(args[0], args[1])
            except Exception as e: 
                print(e)

        case ["es", *args]:
            if len(args) != 2:
                print("incorrect number of arguments")
                continue
            try:
                editSubject(args[0], args[1])
            except Exception as e:
                print(e)
        case ["ss"]:
            showSubjects()
        
        # ---------- session commands ----------
        case ["ap", *args]:
            if len(args) != 2:
                print("incorrect number of arguments")
                continue
            try:
                addPeriod(args[0], args[1])
            except Exception as e:
                print(e)
        case ["dp", *args]:
            if len(args) != 2:
                print("incorrect number of arguments")
                continue
            try:
                deletePeriod(args[0], args[1])
            except Exception as e:
                print(e)
        case ["sp"]:
            showPeriods()

        # ---------- other commands ----------
        case ["h"]:
            printCommands()
        case ["E"]:
            print("Exiting program")
            break

        # ---------- debugging ----------
        case ["d"]:
            print(getData())
        case ["c"]:
            clear()
        case other:
            print('Command not implemented/does not exist')
            printCommands()
