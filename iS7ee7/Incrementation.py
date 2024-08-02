x = 0
print(x)# => 0
x = x + 1
print(x)# => 1
x = x + 1
print(x)# => 2
x = x + 1
print(x)# => 3
#or:
x += 1
print(x)# => 4
x += 1
print(x)# => 5

fruits = ["orange", "lemon", "watermelon"]
i = 0

for fruit in fruits:
	i += 1
	print(fruit)
	#orange
	#lemon
	#watermelon

print(i)# => 3

name = "mohammed"
v = 0

for letter in name:
	v += 1
	print(letter)#m o h a m m e d

print(v)# => 8

f = 0
for letter in name:
	f += 1

print(f)# => 8

print(name + " has " + str(f) + " letters")#mohammed has 8 letters

name_2 = "khaled"
h = 0

for letter in name_2:
	h += 1

print(name_2 + " has " + str(h) + " letters")#khaled has 6 letters

# Question:
name = input("What is your name? ")#maho esmak
x = 0

for letter in name:
	x += 1

print(name + " has " + str(x) + " letters")#(leasm) has (3adad le2a7ref) letters