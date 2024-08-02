#one Virbol:
is_hungry = True

if is_hungry == True:#must be True run
	print("go eat")

#pals else:
is_hungry1 = False
if is_hungry1 == False:#must be False run
	print("go eat")
else:
	print("do not eat")

#pals or:
is_hungry2 = True
wants_to_eat = False

if is_hungry2 or wants_to_eat:#must be One True For run
	print("go eat")
else:
	print("do not eat")

#pals and:
is_hungry3 = True
wants_to_eat1 = True

if is_hungry3 and wants_to_eat1:#must be Two True For run
	print("go eat you are hungry or you just want to eat")
else:
	print("do not eat")

#pals elif(and not):
is_hungry4 = True
wants_to_eat2 = False

if is_hungry4 and wants_to_eat2:
	print("go eat you are hungry or you just want to eat")
elif is_hungry4 and not wants_to_eat2:#must be is_hungry4 True For run
	print("eat so you can survive")
else:
	print("do not eat")

#pals Two elif:
is_hungry5 = False
wants_to_eat3 = True

if is_hungry5 and wants_to_eat3:
	print("go eat you are hungry or you just want to eat")
elif is_hungry5 and not wants_to_eat3:#must be wants_to_eat3 True For run
	print("eat so you can survive")
elif not is_hungry5 and wants_to_eat3:#must be wants_to_eat3 True For run
	print("eat so you can survive")
else:
	print("do not eat")

input("run")