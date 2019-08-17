# można w Pythonie porównywać kilka wartości w jednym wyrażeniu
result = 2 < 3 < 4
print(result)

print(result == True)

result_next = 2 < 4 > 4

# możemy w taki sposób wykonać operację negacji 
print(result != result_next)

# a także w sposób bardziej z naturalnego języka
final_result = result_next is not result
print(final_result)

# and
# w Pythonie nie ma tak jak w Javie operatora '&&',
# żeby wykonać taką operację używamy słowa `and`

and_result = ((2 + 2) == 4) and 5 < -1
print(and_result) 

# or
# kolejny operator różni się od tego z rodziny języków C
# wykonajmy poprzedni kod z operatorem `or`
and_result = ((2 + 2) == 4) or 5 < -1
print(and_result) 

# można też wykonywać porównania logiczne w inny sposób
# zanegujmy wynik
equals_negated = not(1 == 1)
# not 1 == 1 , możemy też opuścić nawiasy
print(equals_negated)