# podstawowa składnia pętli for

# iteracja po liście
name_list = ['Asia', 'Ania', 'Ola', 'Krysia']
for name in name_list:
	print(name) 

# możemy iterować po zwykłym stringu czy tuplu
# aby uniknąć używania zmiennej w pętli możemy nie wyznaczać zmiennej:
for _ in name_list:
	print('next_iteration')

# ciekawa rzecz jest taka, że można iterować przyjmując więcej niż jedną zmienną!
# tu jest przykład z zagnieżdżoną listą list, ale można bez problemu wpakować tuple lub co innego
# można także opuścić nawiasy z wyznaczanej zmiennej
list_of_lists = [
	['name', 'Karol'],
	['age', '26'],
	['gender', 'male']
]

print('One man said us about him:')
for (field, value) in list_of_lists:  # for field, value in list_of_lists:  tak też jest poprawnie
	print(field + ': ' + value)


# podstawowa składnia pętli while

counter = 10

while counter > 0:
	print('Counter is bigger that zero')
	counter = counter - 1
# można też użyć tutaj else, czyli co się wykona jak pętla nie spełni swojego warunku
else:
	print("Counter is less that zero... Let'go!")

# Słowa kluczowe break, continue, pass
# `break` przerywa pętlę jeśli warunek się nie spełnia
# `continue` nie wykonuje iteracji, tak jakby jej nie było, ale cała pętla wraca do wyżej wykonywanej operacji, po prostu omija daną iterację
# `pass` nie robi nic, często można go użyć, żeby wypełnić jakąś operację pustym wykonaniem, bo interpreter nie przepuszcza