import sys
from commands import init,add,toggle,check,uncheck,remove,list

if __name__ == "__main__":
    
    command = sys.argv[1]
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

