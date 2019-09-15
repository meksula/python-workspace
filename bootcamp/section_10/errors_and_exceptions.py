# W Pythonie mamy do dyspozycji 3 słowa kluczowe jeśli chodzi o wyjątki
#
# * try       - wykonanie kodu podatnego na błąd i potencjalnie rzucającego exception
# * except    - klauzula kodu wykonywana po rzuceniu wyjątkiem
# * finally   - kod wykonywany bez względu na rezultat


def fetch_user(username):
   print('Session opended.')
   try:
      username.upper()
   except:			# tutaj możemy albo przechwycić wszystko, albo dać `except TypeError:`
      username = 'unknown'	# możemy sobie definiować wiele różnych `except` i różnie obsłużyć różne wyjątki
      print('Error in username argument')
   finally:
      print('Session closed.')


# wywołanie nie ze stringiem

fetch_user(445)
