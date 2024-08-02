#Without Variables:
print("hello")# => hello

#Ba Variables:
X = "hello"
print(X)# => hello

name = "khaled"
print(name)# => khaled

first_name = "khaled"
last_name = "mohammed"
print(first_name)# => khaled
print(last_name)# => mohammed

print(first_name + last_name)# => khaledmohammed
print(first_name + " " + last_name)# => khaled mohammed

print("my name is " + first_name + " " + last_name)#my name is khaled mohammed

name = "simo" #String
age = 24 #Integer
score = 99.9 #Float
engineer = False #Boolean
#print("my name is "+name+" and my age is "+ age)#TypeError

#1
age = "24"#from Integer to String
#2
print("my name is "+name+" and my age is "+ str(age))#my name is simo and my age is 24

#print("my score is "+score)#TypeError
print("my score is "+ str(score))#my score is 99.9

#print("is "+name+" Engineer? "+ engineer)#TypeError
print("is "+name+" Engineer? "+ str(engineer))#is khaled Engineer? False

#Addition:
num1 = 3
num2 = 5

print(num1 + num2)#3 + 5 => 8

#Subtraction:
num1 = 5
num2 = 7

print(num1 - num2)#5 - 7 => -2

#Multiplication:
num1 = 0
num2 = 54

print(num1 * num2)# 0 * 54 => 0

#Division:
num1 = 9
num2 = 3

print(num1 / num2)# 9 / 3 => 3.0

num3 = "7"
#print(num2 + num3)#TypeError
print(num2 + int(num3))