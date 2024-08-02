# Nested Lists

students = [["mohamed", 19], ["khaled", 20], ["ali", 18]]
#					0				1				2

print(students[0])# => ["mohamed", 19]
print(students[0][0])# => mohamed
print(students[0][1])# => 19
print(students[2][0])# => ali
print(students[2][1])# => 18

#Pals for loop:
for student in students:
	print(student)

for student in students:
	print(student[0] + " " + str(student[1]))