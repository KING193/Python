# 1- import string module
# 2- store all characters in lists (upper/lower case, digists, punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digists and punctuations

#* Import Libraries:
import string
import random

#* Make variable:
s1 = list(string.ascii_lowercase)#? حروف_الأبجدية_الصغيرة
s2 = list(string.ascii_uppercase)#? حروف_الأبجدية_كبيرة
s3 = list(string.digits)#? أرقام
s4 = list(string.punctuation)#? رمواز

characters_number = input("How many characters for the password?: ")

#* Chick value for characters_number:
while True:
	try:
		characters_number = int(characters_number)
		if characters_number < 6:
			print("you need a least 6 characters")
			characters_number = input("Please enter the number again: ")
		else:
			break
	except:
		print("Please enter number only")
		characters_number = input("Please enter the number again: ")

#* Mix the variable:
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#* Add the Centennial Celebration:
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

for i in range(part1):
	password.append(s1[i])
	password.append(s2[i])

for i in range(part2):
	password.append(s3[i])
	password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

#todo Output:
print(password)