print(3**3)# => 27
print(2**3)# => 8

def power(baseNum, powNum):
	result = 1
	for index in range(powNum):
		result = result * baseNum
	return result

print(power(2, 2))# => 4
print(power(2, 3))# => 8
print(power(3, 3))# => 27
print(power(8, 30))# => 1237940039285380274899124224
print(power(5, 5))# => 3125

def power_2(baseNum):
	return baseNum * baseNum

print(power_2(2))# => 4
print(power_2(3))# => 9
print(power_2(5))# => 25

def power_3(baseNum):
	return baseNum * baseNum * baseNum

print(power_3(2))# => 8
print(power_3(3))# => 27
print(power_3(5))# => 125 

input("run")