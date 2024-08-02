# For Loops:

	#Before:
print("hello")#hello
print("hello")#hello
print("hello")#hello
print("hello")#hello
print("hello")#hello

print("hello" * 5)# hellohellohellohellohello

print("hello\n" * 5)#hello
#hello
#hello
#hello
#hello
print("1\n" * 5)#1
#1
#1
#1
#1

	#After:
for x in range(5):
	print("hello")

for x in range(15):
	print("hello " + str(x))

for x in range(1, 10):
	print("hello " + str(x))	

for x in range(0, 105, 5):
	print("hello " + str(x))

# Pals Variables:
name = "mohamed"
for x in name:
	print(x)
	#m
	#o
	#h
	#a
	#m
	#e
	#d

for letter in name:
	print(letter)
#nafs natag

# List
fruits = ["orange", "apple", "lemon", "watermelon"]
for fruit in fruits:
	print(fruit)
	#orange
	#apple
	#lemon
	#watermelon

# Nested For loops:

for x in range(5):
	for i in range(3):
		print("hi")# 5 * 3 => 15 hi

cars = ["ferrari", "aston martin", "bmw"]
adjectives = ["fast", "expensive"]

for car in cars:
	print(car + ":")
	for adj in adjectives:
		print("-" + adj)
	print("\n")