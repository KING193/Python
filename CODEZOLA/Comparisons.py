def max_num(num1, num2, num3):
        if num1 >= num2 and num1 >= num3:#hal num1 akbar ao yasawy num2 => False or True and hal num1 akbar ao yasawy num3 => true or fslse
                return num1#akhary sater fy if
        elif num2 >= num1 and num2 >= num3:#hal num2 akbar ao yasawy num1 => False or True and hal num2 akbar ao yasawy num3 => true or fslse
                return num2#akhary sater fy elif
        else:
                return num3#akhary sater fy else

print(max_num(2, 10, 5))#10 hoe akbar num

#def python /:
print(max(7567, 56, 86, 8))#7567 hoe akbar num

#Add == :
def match_steing(str1, str2):
	if str1 == str2:
		print("the strngs do match")#str1 = str2
	else:
		print("the strings dont match")#str1 not= str2

match_steing("code", "lol")#the strings dont match 

#Add != :
def match_steing_2(str1, str2):
	if str1 != str2:
		print("the strngs do match")#str1 not= str2
	else:
		print("the strings dont match")#str1 = str2

match_steing_2("code", "lol")#the strngs do match

#Add > :
def match_steing_3(str1, str2):
	if str1 > str2:
		print("the strngs do match")#str1 > str2
	else:
		print("the strings dont match")#str1 < str2

match_steing_3(8, 5)#the strngs do match

#Add >= :
def match_steing_4(str1, str2):
	if str1 >= str2:
		print("the strngs do match")#str1 >= str2
	else:
		print("the strings dont match")#str1 < str2

match_steing_4(381, 98)#the strngs do match

#Add < :
def match_steing_5(str1, str2):
	if str1 < str2:
		print("the strngs do match")#str1 < str2
	else:
		print("the strings dont match")#str1 > str2

match_steing_5(87, 233)#the strings dont match
#Add <= :
def match_steing_6(str1, str2):
	if str1 <= str2:
		print("the strngs do match")#str1 <= str2
	else:
		print("the strings dont match")#str1 > str2

match_steing_6(56, 98654)#the strings dont match

input("run")