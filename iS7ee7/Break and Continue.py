# Break and Continue

	#Before:
name = input("What is your name? ")
if name: #True
	print("Nice to meet you " + name)
else:
	print("Please enter your name")

	#After:
while True:
	name = input("What is your name? ")
	if name: #Ture
		print("Nice to meet you " + name)
		break # khorog mon lob
	else:
		print("Please enter your name")

number = input("choose a number: ")
number = int(number)
x = 0

while x < 10:
	x += 1
	if x == number:
		continue # takhaty
	print(x)