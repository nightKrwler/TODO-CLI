import sys

from todo.commands import *

def main():
   
    command = sys.argv[1]
    #print(command)
    if command == "init":
        init()
    elif command == "add":
        add()
    elif command == "list":
        list()
    elif command == "toggle":
        toggle()
    elif command == "check":
        check()
    elif command == "uncheck":
        uncheck()
    elif command == "remove":
        remove()
    elif command =="delete":
        delete()
    else:
        print("ERROR : Please check the command used")
    return