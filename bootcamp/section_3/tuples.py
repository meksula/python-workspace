# Tuple są niemutowalne w przeciwieństwie do listy

lotto_numbers = (3, 16, 19, 34, 36, 41)

print(type(lotto_numbers))
print(len(lotto_numbers))

# możemy wykonać metody np.
result = lotto_numbers.count(19)  # policzy ile w tuplu jest takich elementów
print(result)

index = lotto_numbers.index(36)  # zwróci index tego elementu
print(index)

