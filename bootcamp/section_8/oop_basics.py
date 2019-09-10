# Basic, short introduction to OOP programming

# class declaration and fields assigning
# Remember to write class name in camelcase!

class BaseUser():

    def __init__(self, id, username, rights):
        self.id = id
        self.username = username
        self.rights = rights

user = BaseUser(12, 'admin', ['edit', 'write', 'delete', 'read'])

print(f'User data -> username: {user.username}, id: {user.id}\nUser has rights:')
for right in user.rights:
    print('*',right)
