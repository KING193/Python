# not
# and
# or

	#not:
if 3 == 3:# True
	print("thats true")

if not 3 == 3:# False
	print("thats true")

if 2 == 3:# False
	print("thats true")

if not 2 == 3:# True
	print("thats true")

	#and:
score = input("What is your score? ")
score = int(score)# str => int

absence = input("What is your absence? ")
absence = int(absence)# str => int

if score >= 90 and absence == 0:#yogab an yakon game3 True
	print("You are excellent")
	#or:
elif score >= 90 or absence == 0:#yogab an takon  wa7d 3alla le2aql True
	print("You are good")
else:
	print("You are acceptable")#ead kolohm False
#2:
score_1 = input("What is your score? ")
score_1 = int(score_1)# str => int

absence_1 = input("What is your absence? ")
absence_1 = int(absence_1)# str => int

question = input("Do you like a student? ")

if score_1 >= 90 and absence_1 == 0 and question == "yes":#yogab an yakon game3 True
	print("Tou are excellent")
	#or:
elif score_1 >= 90 or absence_1 == 0 or question == "yes":#yogab an takon  wa7d 3alla le2aql True
	print("You are good")
else:
	print("You are acceptable")#ead kolohm False