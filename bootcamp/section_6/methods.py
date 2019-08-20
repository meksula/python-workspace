# Podstawowa składnia funkcji / metody

def print_my_name(name):
	print(name)
	
name = 'Karol'

print_my_name(name)

# funkcja zwracająca wartość
def add(a, b):
	return a + b
	

# jak zrobić opcjonalny argument funkcji?
# możemy przypisać z góry wartość, wtedy będzie ona opcjonalna
def print_current_year(year = 2019):
	print(f'It is {year} today!')
	
print_current_year()