text = open('bools.py')

all_lines = text.readlines()   # czyta plik tekstowy do listy wierszy

print(all_lines[2])  


# po zakończeniu pracy na pliku nie zapomnij go zamknąć 
# unikniesz dzięki temu błędów
text.close()

# w poniższym kodzie ustawiamy `mode` na wartość readable, a możemy np. Ustawić 'w' czyli writeable
# i wtedy nie możemy czytać tego pliczku za pomocą read()
# a na przykład 'a' może dodawać nowe linie do pliku, bo oznacza 'append'
# 'r+' daje możliwość i zapisu i odczytu
with open('bools.py', mode='r') as some_file:
   print(some_file.read())
