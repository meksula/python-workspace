# ciekawe jak możemy zserializować stringa do listy znaków:

from random import randint

name = 'Karol'
# zadziałało spłaszczanie, flattening
list_of_letters = [letter for letter in name]
print(list_of_letters) 


# To działa! (próba własna)
current_id = 0

def next_id():
	global current_id
	current_id = current_id + 1
	return current_id

letters_with_ids = [
	{
		'id': next_id(), 
		'letter': letter
	} for letter in name
]
print(letters_with_ids)



# inicjalizując listy w taki sposób możemy nawet używać instrukcji warunkowej!
# czyli możemy robić sobie listę od razu zmapowaną na jakąś wartość
even_numbers = [number for number in range(0, 20) if number % 2 == 0]
print(even_numbers)


# Teraz dwa kawałki kodu będą robiły to samo (zagnieżdżona pętla)
# Warte zapamiętania, że Python daje taką ciekawą możliwość!
# Wersja nr. 1 
some_list = []
for x in [2, 4, 6]:
	for y in [1, 10, 1000]:
		some_list.append(x * y)

# Wersja nr. 2
some_list_2 = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]


