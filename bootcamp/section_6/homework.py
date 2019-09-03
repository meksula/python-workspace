import string                   #
print(string.ascii_lowercase)   # Tak szybko można wypisać alfabet


# Compute volume of a sphere
# PL: objętość kuli
# wzór to: 4/3 * PI * r (do potęgi 3)

import math

def sphere_volume(radius):
    return 4/3 * math.pi * (radius**3)

print(sphere_volume(25))


# Check if number is in given range

def is_in_range(num, start, end):
    if start > end:
        print('Conflict!')
        return 
    if num in range(start, end):  # w Pythonie mamy taką sprytną funkcję wbudowaną więc nie musimy klepać ifów
        return True
    else:
        return False

print(is_in_range(5, 3, 100))


# Compute up and low letters in sentence

sentence = 'In my opinion Python is quiet good Programming Language as first language.'

def count_up_and_low(sentence):
    stats = {'low': 0, 'up': 0}
    for letter in sentence:
        if letter.isupper():
            stats['up'] += 1
        else:
            stats['low'] += 1
    return 'Found ' + str(stats['low']) + ' low letters and ' + str(stats['up']) + ' up letters.'

print(count_up_and_low(sentence))


# Return unique elements of collection

collection = [1,1,1,1,2,2,2,3,3,3,3,44,4,4]

def unique(collection):
    unique_list = []
    for item in collection:
        if item not in unique_list:  # znowu zauważ jak fajne operatory daje nam Python!
            unique_list.append(item)
    return unique_list

print(unique(collection))


# Pallindrome - check if word is the same if letters will reversed

def pallindrome(word):
    return word == word[::-1]



# Check if sentence has all letters in alphabet

def has_all(sentence):
    letters = {}
    for letter in string.ascii_lowercase:
        letters[letter] = 0

    for letter in sentence:
        letters[letter] += 1

    for letter in letters:
        if letters[letter] == 0:
            return False

    return True

print(has_all('dcnkc'))



