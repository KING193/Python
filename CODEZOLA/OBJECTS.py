from CLASSES import Employee
from CLASSES import Student

#Class Employee:
employee1 = Employee("islam", 50, "Codezilla", True)
employee2 = Employee("ibrahim", 60, "Facebook", False)

print(employee1.name)# => islam
print(employee1.age)# => 50
print(employee1.department)# => Codezilla
print(employee1.is_manager)# => True

print(employee2.name)# => ibrahim
print(employee2.age)# => 60
print(employee2.department)# => Facebook
print(employee2.is_manager)# => False

print(employee1.name, employee1.age)# => islam 50
print(employee1.name, employee1.age, employee1.department)# => islam 50 Codezilla
print(employee1.name, employee1.age, employee1.department, employee1.is_manager)# => islam 50 Codezilla True

print(employee2.name, employee2.age)# => ibrahim 60
print(employee2.name, employee2.age, employee2.department)# => ibrahim 60 Facebook
print(employee2.name, employee2.age, employee2.is_manager)# => ibrahim 60 False

print(employee1.name, employee2.name)# => islam ibrahim
print(employee1.age, employee2.age)# => 50 60

print(employee1.age, employee2.age, employee2.department, employee1.is_manager)# => 50 60 Facebook True

#Class Student:
student1 = Student("mohamed", 25, 3.5, "computer science", "ain shams")

print(student1.name)# => mohamed
print(student1.name, student1.major)# => mohamed computer science
print(student1.name, student1.major, employee1.name)# => mohamed computer science islam

input("run")