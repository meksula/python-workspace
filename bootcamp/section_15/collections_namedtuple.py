# namedtuple to ciekawa sprawa jeśli nie ma potrzeby tworzyć nowej klasy obiektów
# Możemy po prostu utworzyć tylko obiekt nabity danymi i tyle. Może być przydatne do np. DTO (tak mi się przynajmniej wydaje)

from collections import namedtuple

basic_data = (1993, 'Karol', 26)  # zwykły Tuple


User = namedtuple('User', 'born_year name age')   # do zmiennej przypisujemy namedtuple(), który jako argument przyjmuje 1. nazwę typu, 2. nazwy pól
admin = User(born_year = '1993', name = 'Karol', age = 26) # inicjalizacja nowego namedtuple

print(admin.name)   # możemy się normalnie odwoływać do zmiennych
print(admin.age)



