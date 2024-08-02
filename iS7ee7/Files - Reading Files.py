# Files - Reading Files

# Open
# Read
# Close

# C:\Users\Administrator\Desktop\Programr\Python\iS7ee7\secret

secret_file = open("secret", "r")# r, w, a
content = secret_file.read()
secret_file.close()
print(content)# => the secret sauce for spicy food is red jalapenos WEATRMLON

	#ValueError:{
#secret_file.close()
#content = secret_file.read()
#print(content)
	#	}

#Pals with:

with open("secret", "r") as content:
	print(content.read())# => the secret sauce for spicy food is red jalapenos WEATRMLON

# print(content)# ValueError

#Pals readline:

with open("secret-2", "r") as content:
	print(content.readline())# => orange
	print(content.readline())# => apple
	print(content.readline())# => lemon
	print(content.readline())# => eatermelon
	print(content.readline())# => cucmber
	print(content.readline())# => cabbage

#Pals readlines:

with open("secret-2", "r") as content:
	print(content.readlines())# => ['orange\n', 'apple\n', 'lemon\n', 'watermelon\n', 'cucmber\n', 'cabbage']

#Pals for loop:

with open("secret-2", "r") as content:
	for fruit in content.readlines():
		print(fruit)

#or:
with open("secret-2", "r") as content:
	for fruit in content.readlines():
		print(fruit, end="")# ezalah lefaragh

#Pals text:
with open("secret-2", "r") as content:
	for fruit in content.readlines():
		print("this is a fruit " + fruit, end="")# this is a fruit apple

#akhtir  3adad le2a7raf:
with open("secret-2", "r") as content:
	print(content.read(50))# 50 7raf

with open("secret-2", "r") as content:
	print(content.read(20))# 20 7raf

#Pals write:

with open("secret", "w") as content:
	print(content.write("hello"))
#the secret sauce for spicy food is red jalapenos WEATRMLON => hello

#Pals a:
with open("secret", "a") as content:
	print(content.write("hello"))# hellohello

with open("secret", "a") as content:
	print(content.write("\nhello"))# hellohello
								   # hello
# python file