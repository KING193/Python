# Functions - Default Parametees

def addition(num1, num2):
	print(num1 + num2)

#addition(2)#TypeError

def addition(num1, num2=0):
	print(num1 + num2)

addition(2)# => 2
#addition()#TypeError

def addition(num1=0, num2=0):
	print(num1 + num2)

addition()# => 0
addition(2, 4)# => 6

# email
# password
# username

def registartion(username=False, email=False, password=False):
	if username and email and password:
		print("Registartion Successful")
	else:
		print("Registartion Unsuccessful")

registartion("s7ee7", "s7ee7@hotmail.com")# => Registartion Unsuccessful

registartion("Simo", "Simo543@gmail.com", 12345678)# => Registartion Successful
#
registartion(email="Simo543@gmail,com", password=12345678, username="Simo")