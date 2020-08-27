# TODO-CLI
Command line tool to manage TO-DO Lists

##Installation with pip

```console
$ pip install <path to the todo-cli folder>
```

Available Commands :
```console

$ todo init #Create a Project

$ todo add "Task 1","Task 2" #add tasks

$ todo list # list all the existing tasks

$ todo toggle # Toggle tasks

$ todo check task-id #Mark a specifc task as done 0- task id can be obtained by printing the list of tasks

$ todo uncheck taskid # Mark a specific task as undone

$ todo remove task-id # deletes a task

$ todo delete #deletes the existing project

```

* all/a argument can be used for the commands check,uncheck,remove to apply the operation to all tasks