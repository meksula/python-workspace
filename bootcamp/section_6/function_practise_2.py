# Kolejna część ćwiczeń

# capitalize first and fourth letter in the word
# simple resolve this task

def capit(word):
	result = ''
	index = 0
	for letter in word:
		if index == 0:
			result = result + word[index].capitalize()
		elif index == 3:
			result = result + word[index].capitalize()
		else:
			result = result + word[index]
		index += 1
	return result
	
result = capit('karol')
print(result)

# reverse words in sentence

sentence = 'My name is Karol and I am 26 years old'

def reverse(sentence):
	splitted = sentence.split()
	result = ''
	index = len(splitted) - 1
	for word in splitted:
		result = result + splitted[index] + ' '
		index -= 1
	return result

# a teraz bardziej eleganckie rozwiązanie:

def reverse_v2(sentence):
	return ' '.join(sentence.split()[::-1]) # slice po całej liście od końca

	
print(reverse_v2(sentence))