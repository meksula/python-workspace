# rozwiązania problemów level 2

# zwróć true jeśli obok siebie na liście znajdują się takie same znaki

list_in = [4, 5, 6, 28, 28, 29]
list_in_nxt = [93, 48, 38, 2, 4, 0]

def is_next_rpt(search, inp_list):
	counter = 0
	for item in inp_list:
		if (counter + 1) < len(inp_list) and item == inp_list[counter + 1]:
			return True
		counter += 1
	return False

print(is_next_rpt(28, list_in))
print(is_next_rpt(93, list_in_nxt))


# kolejne zadanie polega na trzykrotnym zwielokrotnieniu każdego znaku w stringu

name = 'Karol'
# multpl describes how much times function should repeat one character
# inp_str is input string to modify
def multp_char(inp_str, multpl):
	result_str = ''
	for char in inp_str:
		for time in range(0, multpl):
			result_str = result_str + char
	return result_str
		
print(multp_char(name, 3))


# W powyższej funkcji się naprodukowałeś, a wystarczyło użyć dobrodzejstw Pythona

def multp_char_v2(inp_str, multpl):
	result = ''
	for char in inp_str:
		result += char * multpl
	return result
	
print(multp_char_v2(name, 3))

