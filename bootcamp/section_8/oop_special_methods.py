# Special/magic/dunder methods allows to use some built-in operations in Python
# such as a length function or the print function with our own created objects
#
# Czyli chodzi o takie funkcje jak w Javie hash(), toString(), equals() etc.
# Specjalne/magiczne metody oznacza się podwójnym podkreśleniem jako prefix i suffix

class Book():

    # metoda konstrukcyjna
    def __init__(self):
        pass

    # reprezentacja jako string
    def __str__(self):
        pass

    # reprezentacja długości obiektu
    def __len__(self):
        pass
    
    # metoda wywoływana po usunięciu obiektu przez słowo kluczowe 'del'
    def __del__(self):
        pass

# BTW: możemy nawet usuwać zmienne z pamięci:
# del <nazwa zmiennej>

harry_potter = Book()
del harry_potter


