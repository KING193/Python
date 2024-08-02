i = 0

while i == 0:
	Login = input("Do you already have an account? (yes/no): ")

	Login = Login.lower()

	if Login == "yes":
		
		secret_file = open("Password_Login", "r")
	
		content = secret_file.read()
		secret_file.close()

		User = input("User Name: ")
		password = input("Password: ")

		file = "User Name: " + User + "\n" + "Password: " + password

		if file == content:
			print("Then log in Successfully")#✔

		else:
			print("Log in Unsuccessfully")#❌

		break
	
	elif Login == "no":
	
		User_Name = input("User Name: ")
		Password = input("Password: ")

		while len(Password) < 8:
			print("Password less than 8 letters or numbers!")#❌
			Password = input("Password: ")

		Confirm_Password = input("Confirm Password: ")
	
		while True:
		
			if Password == Confirm_Password:
				print("Then Successfully create an account")#✔
				
				with open("Password_Login", "w") as Password_file:
					Password_file.write("User Name: " + User_Name + "\n")
					Password_file.write("Password: " + Password)
				
				i += 1
				break
			else:
				print("Wrong password!")#❌
				Confirm_Password = input("Confirm Password: ")
	
	else:
		continue