# Dictionaries
# Keys
# Values

# You can't index, you can't have repeated keys
# Keys: values

student_age = {"ali":22, "mohamed":33, "khaled":19}

students_age = {"ali":22,
				"mohamed":33,
 				"khaled":19,
 				17:"simo"}

print(students_age)# => {'ali': 22, 'mohamed': 33, 'khaled': 19, 17: 'simo'}

#Pals get:
print(students_age.get("khaled"))# => 19
print(students_age.get(17))# => simo

months = {1: "January",
		  2: "Feburary",
		  3: "March",
		  4: "Apri",
		  5: "May",
		  6: "June",
		  7: "July",
		  8: "August",
		  9: "September",
		  10: "October",
		  11: "November",
		  12: "December"}

print(months.get(5))# => may

#Pals update:
students_age.update({"khaled":20})# From 19 to 20
print(students_age)# {'ali': 22, 'mohamed': 33, 'khaled': 20, 17: 'simo'}

#Pals:
students_age["osama"] = 37
print(students_age)# {'ali': 22, 'mohamed': 33, 'khaled': 20, 17: 'simo', 'osama': 37}
			# 02:28:11
#Pals pop:
students_age.pop("osama")
print(students_age)# {'ali': 22, 'mohamed': 33, 'khaled': 20, 17: 'simo'}

del students_age["ali"]
print(students_age)# {'mohamed': 33, 'khaled': 20, 17: 'simo'}

#Pals popitem:
students_age.popitem()
print(students_age)# {'mohamed': 33, 'khaled': 20}

#Pals for loop:
for month in months:
	print(month)#❌

for month in months:
	print(months.get(month))

for month in months:
	print(str(month) + " " + months.get(month))

for keys, values in months.items():
	print(str(keys) + " " + values.upper())