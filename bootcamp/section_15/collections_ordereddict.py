# normalny słownik nie utrzymuje żadnego porządku, kolejność jest jak w HashMap w Javie
# aby utrzymać kolejność możemy użyć obiektu OrderedDict

from collections import OrderedDict

some_map = OrderedDict()
some_map[1] = 'Hey'
some_map[2] = 'now',
some_map[3] = 'the',
some_map[4] = 'dream',
some_map[5] = 'dont',
some_map[6] = 'over'

print(some_map)
