# Nested statements and scopes
# Bardzo ważna sekcja!

x = 25

def var_print():
    x = 50         # zmienna lokalna funkcji (local variable)
    return x

print(var_print()) # 50

# Istnieje coś takiego jak LEGB Rule (wygoogluj jak byś nie pamiętał)
# Z grubsza chodzi o to, że Python szuka sobie zmiennych po kolei:
# L: Local
# E: Enclosing function local
# G: Global
# B: Build-in
# 
# Jak nie znajdzie w local scope to idzie dalej aż do końca.
# Bardzo prosty i logiczny mechanizm, nie tak jak w tym chorym JS

name = 'Karol'

def print_name():
    global name  # w taki sposób mogę wewnętrzną zmienną uczynić globalną
    print(name)

print_name()

# Dlaczego najlepiej unikać zmiennych globalnych?
# Ponieważ przy dużych skryptach możemy się pomylić i łatwo nadpisać zmienną globalną,
# a także takie zmienne są trudne do debugowania
