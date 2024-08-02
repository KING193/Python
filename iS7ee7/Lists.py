# Lists

	#Before:
student1 = "mohamed"
student2 = "ali"
student3 = "khaled"

	#After:
students = ["mohamed", "ali", "khaled", 12, 11.32, 12, True, False]
print(students)#['mohamed', 'ali', 'khaled', 12, 11.32, 12, True, False]

print(students[0])# mohamed
print(students[1])# ali
print(students[4])# 11.32
print(students[7])# False

scores = [13, 11.5, 13, 19, 11, 19.25, 9.5, 11, 8, 16, 16.5]
x = 1

for score in scores:
	print("Score " + str(x) + ": " + str(score))
	x += 1
#Pals index:
print(students.index("khaled"))# 2
#Pals count:
print(students.count("khaled"))# 1
#Pals pop:
print(students.pop())# False
print(students)
#Pals append:
print(students.append("Simo"))# None
print(students)
#insert:
students.insert(0, "nasser")
print(students)
#Pals remove:
students.remove("mohamed")
print(students)
#Pals reverse:
students.reverse()
print(students)
#Pals clear:
students.clear()
print(students)# []