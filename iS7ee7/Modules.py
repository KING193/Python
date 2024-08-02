# Modules
	#1:
import random
import turtle
	#2:
import random as rand
import turtle as snake
	#3:
from random import randint
from turtle import forward, right
#1
random_number = random.randint(0, 100)
print(random_number)

turtle.forward(1000)

for x in range(16):
	turtle.forward(90)
	turtle.right(90)

#2
random_number = rand.randint(0, 100)
print(random_number)

snake.forward(1000)

for x in range(16):
	snake.forward(90)
	snake.right(90)

#3
random_number = randint(0, 100)
print(random_number)

forward(1000)

for x in range(16):
	forward(90)
	right(90)