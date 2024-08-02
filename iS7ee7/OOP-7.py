class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "i don not know what to say" #star

    def display_information(self):
        return self.name, self.age
        
class Cat(Animals):
    def speak(self):
        return "Meow"
    
class Lion(Animals):
    def speak(self):
        return "Hrrrrrr"
    
class Dog(Animals):
    pass

c1 = Cat("biko", 4)
l1 = Lion("joe", 33)

#speak
print(c1.speak())# => Meow
print(l1.speak())# => Hrrrrrr

#cat
print(c1.name)# => biko
print(c1.age)# => 4

#lion
print(l1.name)# => joe
print(l1.age)# => 33

#display
print(c1.display_information())# => ('biko', 4)
print(l1.display_information())# => ('joe', 33)

#dog
d1 = Dog("rix", 10)
print(d1.name, d1.age)# => rix 10
print(d1.speak())# => i don not know what to say