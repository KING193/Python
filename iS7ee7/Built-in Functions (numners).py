# Built-in Functions (numbers):

	#abs:
number = -3
print(abs(number))# -3 => 3

	#round:
number_1 = -5.4
number_2 = -5.6
print(round(number_1))# -5.4 => -5
print(round(number_2))# -5.6 => -6

	#sum:
print(sum([4, 5, 6]))# 4 + 5 + 6 => 15
print(sum([4, 5, 6, 39, 44]))# 4 + 5 + 6 + 39 + 44 => 98

number_3 = [6, 5, 6, 39, 44]
print(sum(number_3))# 6 + 5 + 6 + 39 + 44 => 100

	#max:
print(max(number_3))# lean 44 ho akebr raqam fy number_3	

	#min:
print(min(number_3))# lean 5 ho asghar raqam fy number_3

# incrementation:

number2 = 3

number2 = number2 + 2
print(number2)# 3 + 2 => 5

number2 += 2
print(number2)# 5 + 2 => 7