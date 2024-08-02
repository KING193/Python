class Employee:

    hospital_name = "Mushafa"
    salary_rise = 1000
    employees_numbers = 0

    def __init__(self, name, age, jop, salary):
        self.name = name
        self.age = age
        self.jop = jop
        self.salary = salary
        Employee.employees_numbers += 1

    def add_to_salary(self):
        self.salary += Employee.salary_rise #history

e1 = Employee("khaled", 33, "doctor", 5000)#? Attributes
e2 = Employee("samir", 34, "nurse", 3000)#? Attributes

print(e1.hospital_name)# => Mushafa
print(e2.hospital_name)# => Mushafa

print(e1.salary)# => 5000
print(e2.salary)# => 3000

#add salary
e1.add_to_salary()
e2.add_to_salary()

print(e1.salary)# => 6000
print(e2.salary)# => 4000

#!
print(Employee.hospital_name)# => Mushafa

#star
print(Employee.employees_numbers)# => 2

e3 = Employee("simo", 17, "coding", 8000)
print(Employee.employees_numbers)#todo => 3