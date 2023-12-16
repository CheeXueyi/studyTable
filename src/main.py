from commandLogic import addSubject, editSubject
from data.datastore import getData, clear
from helpers import printCommands

# main loop
printCommands()
while(True):
    command = input("\nCommand: ")
    match command.split():
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

        case ["h"]:
            printCommands()
        case ["E"]:
            print("Exiting program")
            break
        case ["d"]:
            print(getData())
        case ["c"]:
            clear()
        case other:
            print('Command not implemented/does not exist')
            printCommands()