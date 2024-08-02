no_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[0]
]

for row in no_list:
	print(row)# [1, 2, 3]
			  # [4, 5, 6]
			  # [7, 8, 9]
			  # [0]

#Pals For Loop:
for row in no_list:
	for column in row:
		print(column)# 1
					 # 2
					 # 3
					 # 4
					 # 5
					 # 6
					 # 7
					 # 8
					 # 9
					 # 0

#Pals *2:
for row in no_list:
	print(row*2)# [1, 2, 3, 1, 2, 3]
				# [4, 5, 6, 4, 5, 6]
				# [7, 8, 9, 7, 8, 9]
				# [0, 0]			  

#Pals For Loop:
for row in no_list:
	for column in row:
		print(column*2)# 2
					   # 4
					   # 6
					   # 8
					   # 10
					   # 12
					   # 14
					   # 16
					   # 18
					   # 0


# TypeError{
	# for row in no_list:
	# print(row*(row+1))
#}

#Pals For Loop:
for row in no_list:
	for column in row:
		print(column*(column+1))# 2
					 			# 6
								# 12
					 			# 20
					 			# 30
					 			# 42
					 			# 56
					 			# 72
					 			# 90
					 			# 0

input("run")