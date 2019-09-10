# Demonstration of inheritance and polimorphism

# Base class

class BaseUser():
    country = 'PL' 

    def __init__(self, id, username, rights):
        self.id = id
        self.username = username
        self.rights = rights
    
    def about(self):
        print('Class: BaseUser')


class AdminUser(BaseUser):    # podajemy nazwę klasy bazowej w argumencie

    def __init__(self, id, username):
        BaseUser.__init__(self, id, username, ['all'])    # wywołujemy sobie konstruktor klasy bazowej w konstruktorze klasy pochodnej 

    def about(self):                                                          # nadpisaliśmy metodę klasy bazowej
        print(f'I am system administrator, and my name is {self.username}')   # self tutaj odnosi się także do klasy bazowej

admin = AdminUser(345, 'admin_karol')
print(admin.username)
admin.about()


# Polimorfizm tak samo jak w innych językach programowania, oznacza klasę, która ma takie same metody i wspólną klasę bazową

class NormalUser(BaseUser):

    def __init__(self, id, username):
        BaseUser.__init__(self, id, username, ['read', 'write'])

    def about(self):
        print(f'I am easy, common user of this system with username {self.username}')


# demonstracja polimorfizmu

admin_usr = AdminUser(293, 'admin_karol')
common_usr = NormalUser(123, 'common_ola')

# oba obiekty mają metodę about() więc można ją wykonać

for user in [admin_usr, common_usr]:
    user.about()



# Klasy abstrakcyjne
# Nie występuje coś takiego w Pythonie, ale można zastosować okrężne rozwiązanie

class Animal():

    def __init__(self, gender):
        self.gender = gender

    def action(self):
        raise NotImplementedError('This is abstract method and it must be implemented by child class')

Animal('Tommy').action()



