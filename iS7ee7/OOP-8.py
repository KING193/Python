class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "i don not know what to say"

    def display_information(self):
        return self.name, self.age
        
class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)#history
        self.color = color

    def speak(self):
        return "Meow"
    
class Lion(Animals):
    def speak(self):
        return "Hrrrrrr"

c1 = Cat("biko", 4, "brown")
l1 = Lion("joe", 33)

print(c1.color)#todo => brown