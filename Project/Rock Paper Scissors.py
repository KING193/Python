import random

Rock = "R"

Paper = "P"

Scissors = "S"

point_player = 0
point_AI = 0

try:
	while True:

		# choose to player for number
		player = input("What do you choose?Type 1 for Rock or 2 for Paper or 3 for Scissors\n=> ")
		player = int(player)

		# printing the player's choice
		if player == 1:
			print("you chose:\n" + Rock)
		elif player == 2:
			print("you chose:\n" + Paper)
		elif player == 3:
			print("you chose:\n" + Scissors)
		else:
			continue

		# randomizing and printing the AI's choice
		AI = random.randint(1, 3)

		print("AI chose:")
		if AI == 1:
			print(Rock)
		elif AI == 2:
			print(Paper)
		elif AI == 3:
			print(Scissors)
			#Getting the results

		# if the ai chose rock
		if player == 1 and AI == 1:
			print("TIE")
		elif player == 2 and AI == 1:
			print("YOU WON")
			point_player += 1
		elif player == 3 and AI == 1:
			print("YOU LOST")
			point_AI += 1
		
		# if the ai chose paper
		if player == 1 and AI == 2:
			print("YOU LOST")
			point_AI += 1
		elif player == 2 and AI == 2:
			print("TIE")
		elif player == 3 and AI == 2:
			print("YOU WON")
			point_player += 1
		
		# if the ai chose scissors
		if player == 1 and AI == 3:
			print("YOU WON")
			point_player += 1
		elif player == 2 and AI == 3:
			print("YOU LOST")
			point_AI += 1
		elif player == 3 and AI == 3:
			print("TIE")
		
		# Saliva question in player to complete a game
		exit = input("Do you want to complete a game? (Y/N): ")
		exit = exit.lower()

		while exit != "y" and exit !="n":
			exit = input("Do you want to complete a game? (Y/N): ")
			exit = exit.lower()
			

		if exit == "y":
			pass
		elif exit == "n":
			# show point player and ai
			print("Point You: " + str(point_player))
			print("Point AI: "+ str(point_AI))
			
			# show results game
			if point_player > point_AI:
				print("YOU ARE YOU WONNERS A GAME!!!")
			elif point_player < point_AI:
				print("AI YOU WONNERS A GAME!!")
			else:
				print("TIE YOU AND AI!")
			
			break

except ValueError:
	# Error message
	print("Sorry that\'s a not a number")