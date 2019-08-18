# krótki wstęp o wbudowanych operatorach / funkcjach Pythona

# range() określa zakres do iteracji
# range(odkąd zaczynamy, dokąd, wielkość kroku)
for number in range(10):
	print(number)


# można w taki sposób np. wygenerować listę od 50 do 100 i tylko parzyste liczby
list_generated = list(range(50, 100, 2))


# w łatwy sposób można skorelować dwie wartości z sobą z dwóch różnych zestawów danych

index = 0
name = 'Karol'

for letter in name:
	print(f'Letter {letter} is placed in index no. {index}')
	index += 1


# funkcja enumerate() tworzy tuple z każdego elementu w danej kolekcji

for enum_tuple in enumerate(name):
	print(enum_tuple)


# możemy sobie też w łatwy sposób zipować dwie listy,
# niestety takiego zipa nie można przypisać bezpośrednio do zmiennej
student_names = ['Karolina', 'Ala', 'Ola']
id_numbers = [1, 2, 3]

print('Lista uczniów:')
for name, number in zip(student_names, id_numbers):
	print(f'{number}. {name}')

# wyniku powyższych funkcji nie można przypisać do zmiennej ale można z nich utworzyć listę
student_list = list(zip(id_numbers, student_names))

# sprawdźmy czy jakiś uczeń znajduje się na naszej liście
result = ('Karolina', 1) in student_list
print(result)


# można też sprawdzać czy coś znajduje się w mapie

color_map = {
	'red': '#f49234',
	'blue': '#f43322',
	'green': '#f94943'
}

is_exist = 'red' in color_map.keys()   # or in values() 
print(is_exist)


# mamy też wbudowane funkcje min() i max()

num_list = [1, 2, 3, 4, -5, 34]
min_value = min(num_list)
max_value = max(num_list)
print(f'Min: {min_value}, max: {max_value}')


# IMPORTANT! Jak importować nowe biblioteki? Jest do tego funkcja!
from random import shuffle, randint
shuffle(num_list)
print(num_list)  # działa! lista jest pomieszana

random_int = randint(0, 49)  # losowa liczba z zakresu
print(random_int)

# input
your_name = input('Type your name: ')
new_id = len(student_list) + 1
student_list.append((new_id, your_name))
print(f'Hello {your_name}, your numer in student list is: {new_id}')


# casting / parsing
my_age = '26'
in_future = int(my_age) + 20
print(f'For 20 years you will be {in_future} years old')