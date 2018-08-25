from src.ToDoListManager import ToDoListManager
from sty import fg

manager = ToDoListManager()
runnable = True


def main():
    print(fg.blue + "Welcome to ToDo list!" + fg.rs)
    print(fg.blue + "[If you want to see help, type `help`]" + fg.rs)
    while runnable:
        manager.flow()


if __name__ == '__main__':
    main()
