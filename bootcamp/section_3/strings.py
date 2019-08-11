# komendy linuxa możemy wywoływać za pomocą metod z przestrzeni `os`
import os

print('Python test')
#output = os.system('ps aux')

############
# string w Pythonie można traktować jako niemutowalną tablicę znaków
nameDisordered = 'alrok'

name = nameDisordered[4] + nameDisordered[0] + nameDisordered[2] + nameDisordered[3] + nameDisordered[1];
print(name);

# Możemy też liczyć znaki w stringu od tyłu:
nameBottom = nameDisordered[-1] + nameDisordered[-5] + nameDisordered[-3] + nameDisordered[-2] + nameDisordered[-4];
print(nameBottom);

print('Is both strings are equals?: ' + str(name == nameBottom))


# Możemy też wyznaczać zakres (jak substring() w javie)
print('After slice: ', name[2:])
print(name[0:2] + nameBottom[2:])
print(name[1:3])

# Można też określić wartość 'kroku' co ile elementów w danym stringu będzie branych pod uwagę
fullNames = name + ' Meksuła'

print(fullNames[::2]) # Program przejdzie po stringu i wybierze co drugą literę

# No i oczywiście możemy podać wszystkie 3 parametry:
print(fullNames[1:5:2]) # od indexu nr. 1 do indexu nr. 5 co drugi znak

# Zauważ, że możesz w ten sposób zrobić reverse() stringa, przechodząc przez index od tyłu:
print(fullNames[::-1])

word = 'Hello World'
result = word[-3]
