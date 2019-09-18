# O co chodzi?
# Mechanizm generatorów pozwala na nie zapychanie pamięci zbędnymi wartościami
# To coś jakby opóźnienie działania metody i otrzymanie rezultatu w razie potrzeby.
# Jak na przykład chcemy stworzyć nową listę bardzo dużej ilości elementów, 
# nie musimy jej tworzyć i przechowywać każdej zmiennej, każdego obiektu w pamięci.
# Zamiast tego można pamiętać tylko poprzednią zmienną i kolejną.
# Pozwala to nie zasrywać pamięci. Przykład takiej funkcji z biblioteki standardowej to np. range()

# Można napisać taką funkcję: (jak podamy wartość `amount` jako wielką liczbę, to się zasra pamięć, zupełnie bez potrzeby)

def create_cubes(amount):
    result = []
    for i in range(amount):
        result.append(i**3)
    return result

# Można zrobić to tak: (efekt będzie taki sam, a pamięć nie zostanie zaśmiecona, ponieważ nie będziemy mieć listy przechowującej te wszystkie elementy)

def create_cubes_gen(amount):
    for i in range(amount):
        yield x**3                  # keyword `yield` oznacza w pl. wydajność 


# Demonstracja na przykłacie ciągu Fibonacciego:

def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a, b          # ta wartość zostanie "zatrzymana" i będzie można do niej się odnieść później, nie wyznaczamy a i b na nowo!
        a, b = b, a + b
                            # zauważ, że nic tutaj nie zwracamy!

for num in fibonacci(20):
    print(num)              # tutaj lecimy po "wstrzymanych" zmiennych przez słowo kluczowe yield

