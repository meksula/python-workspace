from datetime import datetime

# Karol Meksuła
# 14-08-2018


class Task:

    def __init__(self, author, title, content):
        self.number = "0"
        self.author = author
        self.title = title
        self.content = content
        self.date = datetime.now()

    def __str__(self):
        return "*" + self.number + "|" + self.author + "|" + self.title + "|" + self.content