for letter in "codezille":
	print(letter)# c o d e z i l l e

for letter in "islam":
	print(letter)# i s l a m

#Pals List:
buddies = ["pikachu", "grandizer", "subzero"]

for buddy in buddies:
	print(buddy)# pikachu grandizer subzero

#Pals range:
for x in range(10):
	print(x)# 0 1 2 3 4 5 6 7 8 9

for x in range(5):
	print(x)# 0 1 2 3 4 

for x in range(5, 20):
	print(x)# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
for x in range(3, 9):
	print(x)# 3 4 5 6 7 8
#Pals len:
print(len(buddies))# 3

for index in range(len(buddies)):
	print(index)# 0 1 2

string = "codezille"
for index in range(len(string)):
	print(index)# 0 1 2 3 4 5 6 7 8

#!!:
for index in range(len(buddies)):
	print(buddies[index])# pikachu grandizer subzero
# buddies[0] buddies[1] buddies[2]

#Pals if:
for index in range(10):
	if index % 2 == 0:
		print(index, " is an even number")
	else:
		print(index, " is an odd number")
		# 0  is an even number
		# 1  is an odd number
		# 2  is an even number
		# 3  is an odd number
		# 4  is an even number
		# 5  is an odd number
		# 6  is an even number
		# 7  is an odd number
		# 8  is an even number
		# 9  is an odd number

buddies = ["pikachu", "grandizer", "subzero", "winner"]

for buddy in range(len(buddies)):
	if buddies[buddy] == "winner":
		print(buddy, " is the winner")
	else:
		print(buddy, " is not the winner")
		# 0  is not the winner
		# 1  is not the winner
		# 2  is not the winner
		# 3  is the winner

#Pals break
for buddy in buddies:
	if buddy == "subzero":
		print(buddy, " is your friend")
		break
else:
	print(buddy, " not found")
		# subzero  is your friend

buddies = ["pikachu", "grandizer", "ahmed", "winner"]

for buddy in buddies:
	if buddy == "subzero":
		print(buddy, " is your friend")
		break
else:
	print("not found")
		# subzero  not found


#Pals continue:
for x in range(3, 10):
	if x == 5:
		continue
	print(x, " is the chosen number")
		# 3  is the chosen number
		# 4  is the chosen number
		# 6  is the chosen number
		# 7  is the chosen number
		# 8  is the chosen number
		# 9  is the chosen number