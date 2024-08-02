import random
import time
import termcolor

print(termcolor.colored("Enter \'exit\' for EXIT and see point!!", "yellow"))

x = [" x ", " + ", " - ", " : "]
point = 0

while True:
	time.sleep(2)
	random_number = random.randint(0, 10)
	random_number_2 = random.randint(0, 10)
	random.shuffle(x)
	
	try:
		if x[0] == " x ":
			s1 = random_number * random_number_2
		elif x[0] == " + ":
			s1 = random_number + random_number_2
		elif x[0] == " - ":
			s1 = random_number - random_number_2
		elif x[0] == " : ":
			s1 = random_number / random_number_2
		else:
			print("ERROR!!!")
	except ZeroDivisionError:
		print("Zero")
		continue
	
	s1 = str(s1)
	print(str(random_number)+ str(x[0]) + str(random_number_2)+" = "+str(termcolor.colored("?", "blue"))+"\n")
	number = input("=> ")

	if number == s1:
		point += 1
		print(termcolor.colored("GOOD", "green") + " +1\n")
	elif number == "exit":
		print(termcolor.colored("Total Points: ", "black") + str(termcolor.colored(point, "yellow")))
		break
	else:
		print(termcolor.colored("BAD: ", "red") +s1+"\n")