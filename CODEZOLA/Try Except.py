value = int(input("Enter a number: "))
print(value)
print("success")# {
	# Number => number
	# 		 => success
	# text   => ValueError: invalid literal for int() with base 10: 'text'
#}

#Pals Try and Except:
try:
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success

except:
	print("invalid input")# text   => invalid input

# result = 10/0 #ZeroDivisionError: division by zero

try:
	result = 10/0
	value = int(input("Enter a number: "))# la she2
	print(value)# la she2
	print("success")# la she2

except:
	print("invalid input")# => invalid input

#Pals Try and Except ZeroDivisionError:
try:
	result = 10/0
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success

except ZeroDivisionError:
	print("you cannot divide by zero")# => you cannot divide by zero

try:
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success
	                # text   => ValueError: invalid literal for int() with base 10: 'text'
	result = 10/0

except ZeroDivisionError:
	print("you cannot divide by zero")# => you cannot divide by zero

#Pals Except:
try:
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success
	                # text   => ValueError: invalid literal for int() with base 10: 'text'
	result = 10/0

except ZeroDivisionError:# yogab an takon except lema3ref qabal except le3edy
	print("you cannot divide by zero")# => you cannot divide by zero
except:
	print("invalid input")# => invalid input

#Error{	# yogab an takon except lema3ref qabal except le3edy
#	try:
#		value = int(input("Enter a number: "))
#		print(value)
#		print("success")
#		result = 10/0

#	except:
#		print("you cannot divide by zero")
#	except ZeroDivisionError:
#		print("invalid input")
#}

#Pals Except ValueError:
try:
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success
	                # text   => ValueError: invalid literal for int() with base 10: 'text'
	result = 10/0

except ZeroDivisionError:# yogab an takon except lema3ref qabal except le3edy
	print("you cannot divide by zero")# => you cannot divide by zero
except ValueError:
	print("invalid input")# => invalid input

#Pals as (name):
try:
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success
	                # text   => ValueError: invalid literal for int() with base 10: 'text'
	result = 10/0

except ZeroDivisionError as err:# yogab an takon except lema3ref qabal except le3edy
	print(err)# => division by zero
except ValueError as err1:
	print(err1)# => invalid literal for int() with base 10: 'text'

print("success")# => success

try:
	result = 10/0	
	value = int(input("Enter a number: "))
	print(value)
	print("success")# Number => number
	                # 		 => success
	                # text   => ValueError: invalid literal for int() with base 10: 'text'

except ZeroDivisionError as err:# yogab an takon except lema3ref qabal except le3edy
	print(err)# => division by zero
except ValueError as err1:
	print(err1)# => invalid literal for int() with base 10: 'text'

print("success")# => success