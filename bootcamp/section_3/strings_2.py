# strings are immutable!

sentence = 'so much depends\nupon\na red wheel\nbarrow\nglazed with rain\nwater\nbeside the white\nchicken'

# zmiana jakiegoś znaku w stringu spowoduje błąd
# sentence[0] = 'S'
# Jeśli chcemy zrobić coś takiego to musimy przypisać nowy string

capitalized_first_letter = 'S' + sentence[1:]
print(capitalized_first_letter)

# Co ciekawe można wykonać 'działanie arytmetyczne' na stringu, powielając go np:
print('ha' * 5)

# Standardowo możemy używać zestawu metod stringa np. split() zwraca tablicę części
print(sentence.split('\n'))
