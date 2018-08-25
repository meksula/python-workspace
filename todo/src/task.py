from datetime import datetime
from enum import Enum

# Karol Meksuła
# 14-08-2018


class Task:

    def __init__(self, author, title, content):
        self.number = "0"
        self.author = author
        self.title = title
        self.content = content
        self.date = datetime.now()
        self.status = Status.UNDEFINED

    def __str__(self):
        return "*" + self.number + "|" + self.author + "|" + self.title + "|" + self.content + "|"\
               + self.date.__str__() + "|" + self.status.__str__()

    def setNumber(self, numberAsString: str):
        self.number = numberAsString

    def setDate(self, date: str):
        self.date = date

    def setStatus(self, status: int):
        if status == 0:
            self.status = Status.EXPECTANT
        if status == 1:
            self.status = Status.DONE
        if status == 2:
            self.status = Status.REJECTED
        if status == 3:
            self.status = Status.UNDEFINED
        if status == 4:
            self.status = Status.FAILED
        else:
            self.status = Status.UNDEFINED

    def info(self):
        print("*** ***")
        print("ID:", self.number)
        print("Author:", self.author)
        print("Title:", self.title)
        print("Content:", self.content)
        print("Date:", self.date)
        print("Status:", self.status)
        print("*** ***")


class Status(Enum):
    EXPECTANT = "expectant"
    DONE = "done"
    REJECTED = "rejected"
    UNDEFINED = "undefined"
    FAILED = "failed"
