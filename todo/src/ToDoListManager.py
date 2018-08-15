
from src.authorization import Authorization
from src.features import ProfileCreate
from src.workflow import Workflow

# Karol Meksuła
# 14-08-2018


class ToDoListManager:

    def __init__(self):
        self.command = None
        self.profile = None
        self.profileCreate = ProfileCreate()

    def flow(self):
        self.getCommand()
        self.action()

    def getCommand(self):
        print("$", end="")
        self.command = input()

    def action(self):
        if self.command == "create profile" or self.command == "c p":
            profile = self.profileCreate.create()
            self.save(profile)

        if self.command == "login":
            tmp = self.profileCreate.loadProfile()
            flag = Authorization().authorize(tmp)
            if flag:
                self.profile = tmp
                Workflow(self.profile)

        elif self.command == "account" or self.command == "a":
            print("Change account:")

    def save(self, profile):
        print(profile)
        file = open("todo_DB.txt", "w")
        file.write(profile.__str__())
