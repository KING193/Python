# Nested if Statement

# 2
# positive numner
# -2
# negative numner
# 0
# zero

numner = int(input("Choose a numner: "))

if numner >= 0:
	if numner == 0:
		print("Zero")
	else:
		print("positive numner")
else:
	print("negative numner")