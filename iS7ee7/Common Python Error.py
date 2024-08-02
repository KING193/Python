# Common Python Error

#Syntax Error:
def green: # nasayat wada3 le2aqos
	return "hi"
	#le7al:
def green():
	return "hi"

#NameError:
major = "software"
mayor += " engineer" # akhat2at fy leasm
	#le7al:
major += " engineer"

#ZeroDivisionError:
num1 = 5
num2 = 0
total = num1 / num2 # la yamkenk leqasema 3alla 0
	#le7al:
total = num2 / num1
		#or:
num1 = 5
num2 = 1
total = num1 / num2

#IndexError:
fruits = ["orange", "apple", "lemon"]
print(fruits[3]) # yabda2 le3ed mon 0
	#le7al:
print(fruits[2])

#KeyError:
person = {"name": "jor", "employee": True}
print(person["age"]) # lemofata7 "age" ghair mowagad
	#le7al:
print(person["name"])

#ValueError:
hubby = "basketball"
int(hubby) # la yamkenk ta7awil nas ela raqam
	#le7al:
hubby = "22"
int(hubby)
		#or:
str(hubby)

#TypeError:
print("Hi my name is hussam and my age is " + 33)
	#le7al:
print("Hi my name is hussam and my age is " + str(33))
		#or:
print("Hi my name is hussam and my age is 33")

#Indentation Error:
	print("hello") # la yamkenk wada3 masafak
	#le7al:
print("hello")
		#or:
if 1 == 1:
	print("hello")