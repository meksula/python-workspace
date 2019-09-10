# Description of attributes and method of class

# W pythonie attributes to jak pola klasy w Javie

class BaseUser():
    country = 'PL'  # class attribute, można się odnosić do takiego atrybutu jak w Javie do pola statycznego `BaseUser.country`

    def __init__(self, id, username, rights):
        self.id = id
        self.username = username
        self.rights = rights

    # method declaration
    def print_country(self):
        # Można zadeklarować zmienną osobno tak jak poniżej,
        # ale można także osadzić tak zwany 'ternary conditional operator' jak Elvis operator w Javie
        # country = 'Poland' if self.country == 'PL' else 'United States'
        print(f"User with id: {self.id} is citizen of {'Poland' if self.country == 'PL' else 'United States'}")


usr = BaseUser(923, 'admin', 'superuser')
usr.print_country()


# (Test) Funkcja, która będzie wykonywała coś na obiekcie
# Działa zajebiście, nie ma żadnych getterów i setterów i odwołujemy się do atrybutów po prostu po kropce

def assign_next_id(base_user):
    return base_user.id + 1

print(f'Next id is: {assign_next_id(usr)}')
