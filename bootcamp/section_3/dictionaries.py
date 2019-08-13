# basic dictionary syntax

simpleMap = {'name': 'Karol', 'surname': 'Meksuła'}

print(simpleMap['name'])

# przykładowa zagnieżdżona struktura danych

nested = {
	'test_cases': {
		'first': 'value_0',
		'second': 'value_1'
	}
}

print(nested['test_cases']['first'])  # możemy się bez problemu dobierać do głębiej zagnieżdżonych struktur danych

# nie ma w słownikach metody służącej do dodawania elementu do słownika,
# zamiast tego używamy po prostu wyznaczenia nowego klucza, albo nadpisujemy stary

nested['test_frames'] = {
	'frame_0': '14:50:39:3392',
	'frame_1': '16:23:49:2939'
}

print(nested)

# standardowo, możemy sobie pobierać wszystkie klucze, a także wszystkie wartości za pomocą dwóch metod:
keys = nested.keys()
values = nested.values()

print(len(keys))
print(len(values))
print('****')


items = nested.items()
print(items)