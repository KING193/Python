# Conditionals

age = input("What is your age?\n-")
age = int(age)# "17" => 17

if age > 17:
	print("you are elgibe to take a driver test")
else:
	print("you are not elgibe to take the driver test")
	exit()

driver_test = input("Have you passed the driver test: ")

if driver_test == "yes":
	print("Congrats, now you can have a driver license")
elif driver_test == "no":
	print("Sorry, you need to take the test again to pass")
else:
	print("you didn't answer correctly")