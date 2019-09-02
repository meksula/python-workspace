# lambda expression polega na tym (tak samo jak w Javie) na dostarczeniu
# funkcji w miejscu przyjęcia argumentu

def square(num):
    return num**2

nums = [2, 5, 6, 7, 8]

# wbudowana funkcja map() przyjmuje jakąś funkcję oraz jej argument
# map(function_to_apply, list_of_inputs)

squared_nums = list(map(square, nums))

print(squared_nums)

print(list(map(lambda num: num**2, nums)))

# ogólnie mówiąc Python wprowadza też kilka funkcyjnych rozwiązań
# i ma wbudowane kilka operatorów funkcyjnych: map, filter oraz reduce

# przykład filter

names = ['Ola', 'Karol', 'Agnieszka', 'Adam', 'Henia']

girl_names = list(filter(lambda name: name[-1] == 'a', names))
print(girl_names)


# przykład reduce

# jak w Javie, wykonuje jakieś obliczenia na dwóch elementach i zwraca je.
# przefiltrujmy teraz imiona chłopców o policzmy wszystkie znaki występujące w tych imionach

from functools import reduce

boys_names = list(filter(lambda name: name[-1] is not 'a', names))
letters_amount = reduce((lambda first, second: len(first) + len(second)), boys_names)
print(f'Total amount of letters in boys names is equals to: {letters_amount}')

# Czy można powyższe dwie linijki napisać jako jedną?

letters_amount_next = reduce((lambda first, second: len(first) + len(second)), list(filter(lambda name: name[-1] is not 'a', names)))

print(f'Is both values equals? {letters_amount == letters_amount_next}')
