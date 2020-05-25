from random import randrange


def guessTheNumber():
	randomNumber = randrange(20)
	guessedNumber = input('Enter your guess')

	if guessedNumber == randomNumber:
		print('Well done you guessed right ' + guessedNumber)
	elif guessedNumber > randomNumber:
		print('Your guess is way too high you need to cut it')
	else:
		print('Your guess is way to short you need to raise it')

guessTheNumber()