import os

from sty import fg
from src.task import Task, Status


# Karol Meksuła
# 14-08-2018


class Workflow:

    def __init__(self, profile):
        self.profile = profile
        self.command = ""
        self.block = None
        self.logged = True
        self.file = None

        print("Now you are login as ", profile.name, profile.surname)
        print("You can perform operations in TODO account")
        print("To log out enter `$logout`")
        print("To exit application enter `$exit`")

        while self.logged:
            self.cursor()
            self.execution()

    def cursor(self):
        print(fg.green + "$" + fg.rs, end="")
        self.command = input()
        return self.command

    def execution(self):
        if self.command == "blocks":
            self.showBlocks()

        if self.command == "show":
            self.showTasksInBlock()

        if self.command == "set block" or self.command == "sb":
            print("Type block name:")
            self.cursor()
            self.block = self.command
            print("Current block:", self.block)

        if self.command.isdigit():
            task = self.presentTask(int(self.command))
            if task is None:
                return
            else:
                task.info()

        if self.command == "add":
            self.addTask()

        if self.command[0] == '-':
            self.signTaskAs()

        if self.command == "destroy":
            self.destroy()

        if self.command == "exit":
            exit()

    def showBlocks(self):
        files = os.listdir('.')
        blocks = []

        for file in files:
            if file.title().lower().__contains__(".block"):
                blocks.append(file.title())
        print("Your todo blocks:")
        print(blocks)

    def showTasksInBlock(self):
        if self.block is None:
            print("Which block use?")
            self.cursor()
            self.block = self.command

        try:
            self.file = open(self.block + ".block", "r")
        except FileNotFoundError as ex:
            self.block = None
            self.showTasksInBlock()

        if self.file.readable():
            content = self.file.readlines()
            tasks = self.loadTasks(content)
            for task in tasks:
                print(task.__str__())
        else:
            print("Empty block or not exist.")

    def destroy(self):
        pass

    def addTask(self):
        if self.block is not None:
            print("Current block:", self.block)

        else:
            print("Type block name:")
            self.cursor()
            self.block = self.command

        self.file = open(self.block + ".block", "a")
        number = self.taskCounter(self.block + ".block")
        task = self.taskCreate(str(number))
        self.file.write("\n" + task.__str__())
        print(fg.green + "Task added correctly." + fg.rs)
        self.file.close()

    def signTaskAs(self):
        print("What status to assign to Task:", self.command, "?")
        taskId = int(self.command)
        print(taskId)
        self.cursor()
        if self.command.isdigit():
            status = int(self.command)
            print(status)
            task = self.presentTask(taskId)
            task.setStatus(status)
            print("Status set.")

        else:
            print(fg.red + "No such task. Only digits." + fg.rs)

    def loadTasks(self, content):
        tasks = []

        counter = 0
        for st in content:
            splited = st.split("|")
            for i in splited:
                i.strip()

            if splited.__len__() > 3:
                id = splited[0]
                author = splited[1]
                title = splited[2]
                content = splited[3]
                task = Task(author, title, content)
                task.setNumber(id)

                if splited.__len__() > 4:
                    date = splited[4]
                    task.setDate(date)

                if splited.__len__() > 5:
                    status = splited[5]
                    task.setStatus(status)

                tasks.append(task)

            counter = counter + 1

        return tasks

    def taskCreate(self, number):
        print("Task name:")
        name = self.cursor()
        print("Content:")
        content = self.cursor()

        task = Task(self.profile.name + " " + self.profile.surname, name, content)
        task.setNumber(number)
        return task.__str__()

    def taskCounter(self, path):
        file = open(path, "r")
        return file.readlines().__sizeof__() + 1

    def presentTask(self, taskId: int):
        if self.block is None:
            print("First, set block.")
            return
        else:
            self.file = open(self.block + ".block", "r")
            content = self.file.readlines()
            tasks = self.loadTasks(content)

            for task in tasks:
                if task.number == "*" + str(taskId):
                    return task
