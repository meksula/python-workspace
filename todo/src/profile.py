
# Karol Meksuła
# 14-08-2018


class Profile:

    def __init__(self, name, surname, password):
        self.name = name
        self.surname = surname
        self.password = password

    def __str__(self):
        return "@" + self.name + "\n@" + self.surname + "\n@" + self.password

    def info(self):
        print("name:", self.name, "surname:", self.surname, "password:", self.password)
