# https://docs.python.org/3/library/collections.html#collections.Counter
# Potężna biblioteka ułatwiająca pracę z kolekcjami
# Counter przyjmuje w argumencie obiekt 'iterable' i tworzy mapę, w której nasze obiekty są kluczami, a wartość to ilość wystąpień tych obiektów

from collections import Counter

some_list = ['a', 'a', 'b', 'y', 'z', 'b']
occurs = Counter(some_list)
print(occurs)

# tak samo Counter działa na stringach
print(Counter('Karol'))

# albo na wyrazach
print(list(Counter('Król Karol kupił królowej Karolinie korale koloru kolorowego'.split()).elements()))


sentence = "Hey now, hey now, the dream don't is over, hey now, hey now!"
sentence_words = sentence.split()
sentence_counted = Counter(sentence_words)
most_common = sentence_counted.most_common(1)
print(f'Most common word in sentence is: {most_common[0][0]}')

words_map = dict(sentence_counted)
print(words_map)


