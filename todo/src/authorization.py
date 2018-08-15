
# Karol Meksuła
# 14-08-2018


class Authorization:

    def authorize(self, profile):
        print("Enter your surname:")
        self.cursor()
        surname = input()

        print("Enter your password")
        self.cursor()
        password = input()

        if surname == profile.surname and password == profile.password:
            print("Authentication successful!")
            return True

        else:
            print("Authentication failed!")
            return False

    def cursor(self):
        print("$", end="")
