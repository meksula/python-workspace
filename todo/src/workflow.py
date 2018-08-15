from src.task import Task

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
        print("$", end="")
        self.command = input()
        return self.command

    def execution(self):
        if self.command == "blocks":
            self.showBlocks()

        if self.command == "show":
            self.showTasksInBlock()

        if self.command == "add":
            self.addTask()

        if self.command == "sign as":
            self.signTaskAs()

        if self.command == "destroy":
            self.destroy()

        if self.command == "exit":
            exit()

    def showBlocks(self):
        pass

    def showTasksInBlock(self):
        print("Which block use?")
        self.cursor()
        if self.block is None:
            self.block = self.command
            self.file = open(self.block + ".txt", "r")

        if self.file.readable():
            content = self.file.readlines()
            self.presentAsTasks(content)
        else:
            print("Empty block.")

    def destroy(self):
        pass

    def addTask(self):
        if self.block is not None:
            print("Current block:", self.block)

        else:
            print("Type block name:")
            self.cursor()
            self.block = self.command
            self.file = open(self.block + ".txt", "a")
            task = self.taskCreate()
            self.file.write("\n" + task.__str__())
            print("Task added correctly.")

    def signTaskAs(self):
        pass

    def presentAsTasks(self, content):
        pass

    def taskCreate(self):
        print("Task name:")
        name = self.cursor()
        print("Content:")
        content = self.cursor()

        task = Task(self.profile.name + " " + self.profile.surname, name, content)
        return task.__str__()
