# Functions - scope
# local
# global

def greet():
	name = "simo"
	return "hi " + name

print(greet())
#yamkenk:
name1 = "s7ee7"
def greet():
	# name1 += " ahmed" # UnboundLocalError
	return "hi " + name1

print(greet())
#UnboundLocalError:
def greet():
	name = "simo"
	name += " ahmed"
	return "hi " + name

print(greet())

	# global:
name_2 = "are"
def look():
	global name_2
	name_2 += " pig"
	return "you " + " " + name_2

print(look())
print(name_2)

#
name_3 = "ali"
def look():
	age = 18
	global name_3
	name_3 += " pig"
	return "you " + " " + name_3

print(look())
print(name_3)

#print(age)# NameError

name_4 = "are"
def look():
	age = 18
	global name_4
	name_4 += " ahmed"
	return age

age = look()
print(age)

print(look())
print(name_4)

age += 1
print(age)

input("run")