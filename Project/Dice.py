import random

dice_drawing = {
	1: (
		"-----",
		"|   |",
		"| O |",
		"|   |",
		"-----",
		),
	2: (
		"-----",
		"|O  |",
		"|   |",
		"|  O|",
		"-----",
		),
	3: (
		"-----",
		"|O  |",
		"| O |",
		"|  O|",
		"-----",
		),
	4: (
		"-----",
		"|O O|",
		"|   |",
		"|O O|",
		"-----",
		),
	5: (
		"-----",
		"|O O|",
		"| O |",
		"|O O|",
		"-----",
		),
	6: (
		"-----",
		"|O O|",
		"|O O|",
		"|O O|",
		"-----",
		),
}

def Dice():
	roll = input("Do you want to roll?(y/n): ")

	while roll == "y":
		
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)

		print("The First Dice: ")
		print("\n".join(dice_drawing[dice1]))

		print("The Second Dice: ")		
		print("\n".join(dice_drawing[dice2]))


		roll = input("Do you want to roll again?(y/n): ")

Dice()