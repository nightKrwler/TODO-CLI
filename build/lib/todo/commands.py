import sys
import json
from colorama import Fore, Back, Style
from constants import PROJECTFILE
from menu_utils import menuInterface
import curses
import re

def check_int(element):
    if re.match(r'^-?\d+(?:\.\d+)?$', element) is None:
        return False
    return True



def write(object):
    outfile = open(PROJECTFILE,"w")
    json.dump(object,outfile)
    outfile.close()

def init():
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)

    if(len(todo_object)!=0):
        print("Project already exists")
    else : 
        name = input("Enter Project Name : ",)
        pdict = {"name": name,
                "todo" : []}
        json.dump(pdict,open(PROJECTFILE,"w"))
        print(f"Project {name} has been created")

def add():

    with open(PROJECTFILE, 'r') as openfile:
        todo_object = json.load(openfile)
    tasks = sys.argv[2]
    tasks_list = tasks.split(",")
    
    for t in tasks_list:
        tdict = {"task":t,
        "status": False}
        print("{} task added".format(t))
        todo_object["todo"].append(tdict)

    write(todo_object)

def list(): 
    done =0
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)
    
    print('{blue}{name:^14}{reset}'.format(
        blue = Fore.BLUE,
        name = todo_object["name"],
        reset = Style.RESET_ALL

    ))
    c =0 
    for i in todo_object["todo"]:
        char = ' ✓ ' if i["status"] else ' x '
        done+= 1 if i["status"] else 0
        color = Fore.GREEN if i["status"] else Fore.RED
        print(
            '{black}{id}{reset}  {color}{char}{reset}  {task}{reset}'
            .format(
                id=c,
                color=color,
                char = char,
                black=Fore.BLACK,
                task=i["task"],
                blue = Fore.BLUE,
                green = Fore.GREEN,
                reset = Style.RESET_ALL,
            ))
        c+=1
    
    total = len(todo_object["todo"])
    print('{info}{items} items: {done} completed, {not_done} to be done{reset}'.format(
        info =Fore.LIGHTBLACK_EX,
        items = total,
        done = done,
        not_done = total-done,
        reset=Style.RESET_ALL
    ))
    
def toggle():
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)
    tasks = todo_object["todo"]  
    mi = menuInterface(tasks)  
    todo_object["todo"] = curses.wrapper(mi.main)
    write(todo_object)
    list()

def check():
    val = sys.argv[2]
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)
    if(check_int(val)):
        id = int(sys.argv[2])
        todo_object["todo"][id]["status"] = True     
    elif(re.match(r'[aA]',val)):
        for id in range(len(todo_object["todo"])):
            todo_object["todo"][id]["status"] = True
    else:
        print("Please check the arguments.")
        return
    write(todo_object)
    list()
    return

def uncheck():
    val = sys.argv[2]
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)
    if(check_int(val)):
        id = int(sys.argv[2])
        todo_object["todo"][id]["status"] = False     
    elif(re.match(r'[aA]',val)):
        for id in range(len(todo_object["todo"])):
            todo_object["todo"][id]["status"] = False
    else:
        print("Please check the arguments.")
        return
    write(todo_object)
    list()
    return

def remove():
    val = sys.argv[2]
    with open(PROJECTFILE, 'r') as openfile: 
        todo_object = json.load(openfile)
    if(check_int(val)):
        id = int(sys.argv[2])
        #print(id,len(todo_object["todo"]))
        if id>=len(todo_object["todo"]):
            print("No Tasks left or Incorrect indices")
        else:
            todo_object["todo"].pop(id)
            write(todo_object)
        list()
        return
    elif(re.match(r'[aA]',val)):
        todo_object = {}
        write(todo_object)
        list()
    else:
        print("Please check the arguments.")



