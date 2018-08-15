from src.ToDoListManager import ToDoListManager

# Karol Meksuła
# 14-08-2018

manager = ToDoListManager()

runnable = True


def main():
    print("Welcome to ToDo list!")
    print("[If you want to see help, type `help`]")
    while runnable:
        manager.flow()


if __name__ == '__main__':
    main()
