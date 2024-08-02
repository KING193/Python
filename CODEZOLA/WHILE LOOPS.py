i  = 1
x = 1
y = 1
k = 1

while i <= 10:
	print(i)
	i = i + 1 #or i += 1

print("the loop has ended-1")

#Pals else:
while x <= 23:
	print("hi")
	x += 2
else:
	print("the condition is not true")

print("\nthe loop has ended-2")

#Pals continue:
while y <= 10:
	y += 1
	if y == 6:
		continue #Skip
	print(y)

print("the loop has ended-3")

#Pals break:
while k <= 10:
	k = k + 1
	if k == 6:
		break #Exit
	print(k)

print("the loop has ended-4")

##loop is not ended:

while True:#7al9 la nih2y
	print("loop not ended")