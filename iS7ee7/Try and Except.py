# Try and Except

age = input("What is your age? ")# fourty => ValueError
age = int(age)

print("Your age is " + str(age))

#Pals Try and Except:
age_2 = input("What is your age? ")

try:
	age_2 = int(age_2)
	print("your age is " + str(age_2))
except ValueError:
	print("please enter a real number")