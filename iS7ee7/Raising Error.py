# Raising Error

def chooseNumber():

	number = input("choose a number from 1 to 10\n")
	number = int(number)

	if number < 1 or number > 10:
		print("Palse insert a number from 1 to 10")
	else:
		print("Your number is " + str(number))


chooseNumber()

#Pals raise ValueError:
def chooseNumber():

	number = input("choose a number from 1 to 10\n")
	number = int(number)

	if number < 1 or number > 10:
		raise ValueError("Palse insert from 1 to 10")
	else:
		print("Your number is " + str(number))


chooseNumber()