# exercise no 1
def lesser_two_even(first, second):
	even = get_even_only([first, second])
	if len(even) == 0:
		print('There is no even numbers on list')
		return 0
	return min(even)
		

# returns even numbers or if has no even, returns 0
def get_even_only(numbers):
	even_numbers = []
	for num in numbers:
		if num % 2 == 0:
			even_numbers.append(num)
	return even_numbers
			
# returns min number from list
def min(numbers):
	min_num = numbers[0]
	for num in numbers:
		if num < min_num:
			min_num = num
	return min_num
						
result = lesser_two_even(10, 6)
print(result)


# excercise no 2
# if both words in string start in this same letter, return true

def is_same_first_letter(input_string):
	parts = input_string.split(', ')
	current_letter = parts[0][0].lower()
	for part in parts:
		if part[0].lower() != current_letter:
			return False
	return True	
	
result_letters = is_same_first_letter('Karol, drut, kamień, korale, Koń')
print('Is all words starts with the same letter? : {}'.format(result_letters))


# excercise no 3

def is_twenty(first, second):
	for num in [first, second]:
		if num == 20:
			return True
	if first + second == 20:
		return True
	return False
	

result_nums = is_twenty(20, 5)
result_nums_next = is_twenty(9, 18)

print('Results: {}, {}'.format(result_nums, result_nums_next))













