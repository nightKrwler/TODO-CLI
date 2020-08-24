import sys
from todo.commands import init, add

if __name__ == "__main__":
    
    command = sys.argv[1]
    print(command)
    if command == "init":
        init()
    '''elif command == "add":
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
        remove()'''
