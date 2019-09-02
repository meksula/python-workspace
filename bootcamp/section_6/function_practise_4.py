# spy game
# zadanie polega na znalezieniu czy na liście w odpowiedniej kolejności
# znajdują się liczby 007

def spy(num_arr):
	arr_as_str = ''
	for num in num_arr:
		if num == 0 or num == 7:
			arr_as_str += str(num)
	if '007' in arr_as_str:
		return True
	else:
		return False
		
print(spy([1, 4, 5, 6, 7, 8, 4]))
print(spy([1, 4, 0, 5, 6, 0, 5, 5, 4, 7, 8, 2, 4]))

# inne świetne rozwiązanie pokazane na filmiku

def spy_v2(num_arr):
	code = [0, 0, 7, 'x']
	for num in num_arr:
		if num == code[0]:
			code.pop(0)
		elif code[0] == 'x':
			return True
	return False
	
print(spy_v2([1, 4, 5, 6, 7, 8, 4]))
print(spy_v2([1, 4, 0, 5, 6, 0, 5, 5, 4, 7, 8, 2, 4]))