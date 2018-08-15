from src.profile import Profile

# Karol Meksuła
# 14-08-2018


class ProfileCreate:

    def __init__(self):
        self.name = None
        self.surname = None

    def cursor(self):
        print("$", end="")

    def create(self):
        print("Please enter your name: ", end="")
        self.name = input()
        self.cursor()
        print("Now, please enter your surname: ", end="")
        self.surname = input()
        self.cursor()
        print("Set your password now: ", end="")
        password = input()
        print(self.name, self.surname, ", your account has just created.")
        return Profile(self.name, self.surname, password)

    def loadProfile(self):
        file = open("todo_DB.txt", "r")
        lines = file.readlines()
        properties = []

        for line in lines:
            char = self.readProperty(line)
            if char == "@":
                length = len(line)
                properties.append(line[1:length].strip())

        return Profile(properties[0], properties[1], properties[2])

    def readProperty(self, value):
        return value[:1]
