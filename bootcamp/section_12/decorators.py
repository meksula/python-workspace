# Dekoratory w Pythonie to bardzo podobna koncepcja do dekoratorów w Angularze, ale trochę inna niż adnotacje w Javie
#
# Składnia jest prosta:

# @decorate_method
# def my_method():
#    pass

# Pamiętaj, że w Pythonie tak jak w np. JavaScript, funkcję traktujemy jak normalną zmienną. Możemy ją zwracać, przypisywać etc.

def example_func(value = 'Some value'):
    
    def inner_func():
        print('inner_func() invoked!')
        return value
    
    return inner_func   # zwracamy funkcję bez jej wywołania


inner_func = example_func()  # przypisujemy do zmiennej rezultat wywołania example_func() 
print(inner_func)            # pokazuje wskaźnik do funkcji jako output 

inner_func()

print('\n***\n')
# Czyli ogólnie rzecz ujmując dekotatory w Pythonie to po prostu sposób na implementację wzorca projektowego Dekorator
# Teraz demonstracja z Pythonową składnią:

def decorate_cake(func):            # deklarujemy funkcję, która przyjmuje inną funkcję, która będzie udekorowana
    def decorating_func():          # piszemy funkcję zagnieżdżoną
        print('Cherry on cake')     # działanie przed wywołaniem funkcji przyjętej w argumencie
        func()                      # wywołanie funkcji, którą przyjęliśmy jako argument
        print('... lay on plate.')  # działanie po wywołaniu funkcji przyjętej w argumencie
    return decorating_func          # zwrócenie funkcji zagnieżdżonej, ale nie wywołanie!

@decorate_cake                      # dekorator - nazwa funkcji, która a argumencie przyjmuje zawsze inną funkcję
def cake():                         # definicja funkcji udekorowanej
    print('This is a cake')         # działanie funkcji udekorowanej

cake()
