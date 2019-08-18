# musimy używać wcięć, bo bez tego interpreter wyrzuci wyjątek
# mamy 3 operatory wyrażeń warunkowych:
#   - if 
#   - elif
#	- else

suffix = '\nWelcome!'
username = 'Karol1'
welcome_text = None
unauthorized = '401 Unauthorized'

if username == 'Ola':
	welcome_text = 'You are logged as Ola'
elif username == 'Jan':
	welcome_text = 'Hi John! You are CEO of our company'
elif username == 'Karol':
	welcome_text = 'Karol - main software architect'
else:
	welcome_text = unauthorized

if welcome_text != unauthorized:
	welcome_text = welcome_text + suffix
else:
	pass

print(welcome_text)
