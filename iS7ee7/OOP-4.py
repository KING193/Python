class Cat:
    def __init__(self, name, age, food):#? Add value and __init__ To work with each copy
        self.name = name#?storage Valued name in name
        self.age = age
        self.email = self.name + "@" + "cats.crm"#todo self.email = self.name + "@" + "cats.crm"
        self.food = food

    def like_food(self):
        return self.food
    
    def meow(self):
        print("meow!")

cat1 = Cat("mark", 17, "tuna")#* name cat1 is mark and age 17 to email mark@cats.crm, tuna
cat2 = Cat("joe", 16, "meat")#* name cat2 is joe and age 16 to email joe@cats.crm, meat

print(cat1.like_food())# => tuna
print(cat2.like_food())# => meat

print(cat1.name)# => mark
print(cat2.name)# => joe

print(cat1.age)# => 17
print(cat2.age)# => 16

print(cat1.email)# => mark@cats.crm
print(cat2.email)# => joe@cats.crm

print(cat1.food)# => tuna
print(cat2.food)# => meat

#todo
print("Hi i am cat my name " + cat1.name + " and my age is " + str(cat1.age) + " He is my frieda " + cat2.name + " you age " + str(cat2.age) + "? " + "Look my email " + cat1.email + " and my email to " + cat2.email + " 0_0! I like " + cat1.food + " what you like food? I don't like " + cat1.food + " I like only " + cat2.food + " (-o-)\'")