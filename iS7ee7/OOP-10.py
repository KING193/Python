class Person:
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_information(self):
        return self.name, self.age
    
    @classmethod #ta3ml bidon object
    def git_population(cls):
        return cls.population
    
    @staticmethod #ta3ml bidon object walk t7tag 9iam mital 17
    def is_adult(age):
        return age >= 18 #True ot False
    
p1 = Person("osama", 33)
print(p1.display_information())# => ('osama', 33)

#star
print(Person.git_population())#todo => 50

print(Person.is_adult(17))# => False

print(Person.is_adult(p1.age))# => True

#COMPLEAT