    # W pythonie można do listy wrzucać obiekty różnych typów:
my_list = [1.29, 'Karol', ['nested']]
print(my_list)

length = len(my_list)

    # Interpolacja stringów: można wyświetlać stringi poprzez wstawienie litery `f` przed samym stringiem
print(f'My list has {length} elements')

    # Ogólnie zasada działania jest podobna, albo nawet taka sama jak działanie stringa
    # W taki sam sposób możemy się posługiwać listami

    # W poniższej linii kodu wyciągam ostatni element z listy, który to jest tablicą i z tej tablicy wyciągam element na zerowym indexie
    # Potem wywołuję metodę powiększającą znaki
print(my_list[-1][0].upper())

    # Tak samo możemy robić slice po liście jak po stringu:
part = my_list[:2]
print(part)

    # Można w bardzo łatwy sposób połączyć listy

new_list = my_list + ['Meksuła', 2019]
print(new_list)


    # Listy są jednak w pełni mutowalne, można podmieniać wartości. 
    # Weźmy teraz listę i wypakujmy z niej stringa

my_list[-1] = my_list[-1][0]
print(my_list)

    # Dodanie elementu na końcu listy:

my_list.append('some item')
print(my_list)

    # Usunięcie ostatniego elementu

my_list.append('unwanted element')
my_list.pop()
    
    # Metoda pop() jest mega, można usunąć element, który się chce! Nie trzeba robić cudów jak w JavaScripcie

my_list.pop(2)
print(my_list)

    # Odwracanie kolejności listy

print(my_list[::-1])
my_list.reverse() # także odwraca kolejność, ale robi to w miejscu i nic nie zwraca!

    # Sortowanie listy

alphabet = ['f', 's', 'a', 'g']
alphabet.sort()  # metoda sortowania nic nie zwraca

print(alphabet)

    # Sprawdzanie typów

print(type(alphabet[0]))


if type(alphabet[0]) == str:
    print('Types are same!')
else: 
    print('Types are NOT same!')


