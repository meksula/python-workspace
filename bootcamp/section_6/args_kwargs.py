# *args and **kwargs (key word arguments)

# *args
# możemy użyć takiego operatora asterisk (ang. gwiazdka) do określenia, 
# że nie wiemy ile argumentów chcemy przyjąć
# np. chcemy sumować dane liczby

def sum_numbers(*args):  # nie ważne jak nazwałeś zmienną po asterisku, ale konwencja mówi, żeby używać właśnie słowa 'args'
	acc = 0
	for num in args:  
		acc += num
	return acc

result = sum_numbers(10, 20, 30)
print(result)

# a więc wniosek jest taki, że dostajemy tuple, w sumie na jedno wychodzi jak byśmy przekazali do metody listę


# **kwargs - operator z podwójnym asterisk dostarczy do metody słownik!

products = {
	'strawberry': {
		'type': 'fruit',
		'name': 'Strawberry',
		'price': 8.23
	},
	'cucumber': {
		'type': 'vegetable',
		'name': 'Cucumber',
		'price': 4.59
	},
	'banana': {
		'type': 'fruit',
		'name': 'Banana',
		'price': 5.99
	}
}


def sum_princes_of_fruits(**kwargs):
	acc = 0
	for key in kwargs:
		item = kwargs[key]
		if item['type'] == 'fruit':
			acc += item['price']
		else:
			print(item['name'] + ' is not fruit!')
	return acc

# wywołanie funkcji z 'wiekszymi obiektami'
result = sum_princes_of_fruits(
	strawberry = {
		'type': 'fruit',
		'name': 'Strawberry',
		'price': 8.23
	},
	cucumber = {
		'type': 'vegetable',
		'name': 'Cucumber',
		'price': 4.59
	},
	banana = {
		'type': 'fruit',
		'name': 'Banana',
		'price': 5.99
	})

print('Summary price: ' + str(result))


def print_colors_available(**kwargs):
	for color in kwargs:
		print(kwargs[color])

print_colors_available(sea = 'blue', sun = 'yellow', sky = 'blue')


# nie ma problemu nawet kiedy chcemy sobie przekazać do funkcji zarówno *args i **kwargs

def find_highest(*args, **kwargs):
	current_highest = 0
	for item in args:
		if kwargs[item] > current_highest:
			print(str(kwargs[item]) + ' compare with: ' + str(current_highest))
			current_highest = kwargs[item]
	return current_highest

highest_salary = find_highest('java', 'ruby', 'python', 'php', 'html', java = 1600, ruby = 2900, python = 2000, html = 900, php = 1000)
print('Best salary is: ' + str(highest_salary))