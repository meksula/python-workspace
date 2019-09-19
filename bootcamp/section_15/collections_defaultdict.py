# Często zdarza się wywołać nieistniejący klucz w słowniku co powoduje `KeyError`.
# defaultdict tworzy słownik, a w konstruktorze przyjmuje funkcję faktoryzującą.
# Jak próbujemy się dostać do klucza który nie istnieje, to defaultfict z automatu nam doda taki klucz z wartością domyślną
# zdefiniowaną w funkcji

from collections import defaultdict
from random import randint

numbers = defaultdict(lambda : randint(1, 10))   # inicjalizacja defaultdict
numbers['First']                                 # wywołanie nieistniejącego klucza
print(numbers['First'])                          # jako output widzimy losową liczbę, określoną w lambdzie
