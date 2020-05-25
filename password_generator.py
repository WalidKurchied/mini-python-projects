import string
import secrets

def getUserInput():
	passLength = customInput('Pasword length ')
	lettersCount = customInput('How many letters ')
	numbersCount = customInput('How many numbers ')

	if passLength < 6:
		print('Password must have a minimum of 6 characters')
	else:
		generatePassword(passLength, lettersCount, numbersCount)

def generatePassword(passRange, letterCount, numbersCount):
	alpha = string.ascii_letters + string.digits + '!@#$%^&*(){}[]?/><.,|":;=-+_'
	password = ''.join(secrets.choice(alpha) for i in range(passRange))
	print('Your password is ' + password)
	
def customInput(label):
	return int(input(label))



# starter
getUserInput();


# Todo add letterscount and numberscount support