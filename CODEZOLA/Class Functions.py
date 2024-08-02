class Employees:
	def __init__(self, name, age, department, is_manager, rating, salary):
		self.name = name
		self.age = age
		self.department = department
		self.is_manager = is_manager
		self.rating = rating # rating is from 1-5
		self.salary = salary

	def is_excellent(self):
		if self.rating >= 4.5:
			return True
		else:
			return False

	def bonus(self):
		if self.age == 60:
			self.salary += 500
			print("salary increased to " + str(self.salary))
		else:
			print("no bonus added, salary is still " + str(self.salary))


employees1 = Employees("yusuf", 51, "Google", True, 5, 1500)
employees2 = Employees("simo", 60, "Apple", False, 3.5, 500)

print(employees1.is_excellent())# => True
print(employees2.is_excellent())# => False

print(employees1.salary)# => 1500
employees1.bonus()# => no bonus added, salary is still 1500
print(employees2.salary)# => 500
employees2.bonus()# => salary increased to 1000