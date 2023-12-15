from data.datastore import getData, clear
from helpers import printCommands

# main loop
printCommands()
while(True):
    command = input()
    match command:
        case "h":
            printCommands()
        case "E":
            print("Exiting program")
            break
        case other:
            print('Command not implemented/ does not exist')
            printCommands()