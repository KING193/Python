no_list = [1, 2, 3, 4]
print(no_list)# => [1, 2, 3, 4]

no_list = [
	[1, 2, 3], # 0
	[4, 5, 6], # 1
	[7, 8, 9], # 2
	[0]		   # 3
]

print(no_list)# => [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

print(no_list[1])# => [4, 5, 6]
print(no_list[2])# => [7, 8, 9]

print(no_list[0][1])# => 2
print(no_list[2][1])# => 8
print(no_list[1][2])# => 6

input("run")