# Functions - Return

def registartion(username=False, email=False, password=False):
	if username and email and password:
		return "Registartion Successful"
	else:
		return "Registartion Unsuccessful"

student1 = registartion("s7ee7", "s7ee7@hotmail.com")# => Registartion Unsuccessful
print(student1)

def registartion(username=False, email=False, password=False):
	if username and email and password:
		return [username, email, password]
	else:
		return "Registartion Unsuccessful"

student1 = registartion("s7ee7", "s7ee7@hotmail.com", 123)# => ['s7ee7', 's7ee7@hotmail.com', 123]
print(student1)

student2 = registartion("mohamed", "mohamed32@gmali.com", 561)# => ['mohamed', 'mohamed32@gmali.com', 561]
print(student2)