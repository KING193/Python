# AUTOMATION-2
import pyautogui
import time

x = 0

while x < 5:
	x += 1
	time.sleep(2)
	print(pyautogui.position())

	# Point(x=698, y=289)
	# Point(x=484, y=213)
	# Point(x=328, y=160)
	# Point(x=193, y=323)
	# Point(x=656, y=89)
	# Point(x=775, y=429)
	# Point(x=304, y=326)
	# Point(x=342, y=575)
	# Point(x=147, y=732)
	# Point(x=974, y=0)
	# Point(x=0, y=4)
	# Point(x=0, y=0)
	# Point(x=1023, y=0)
	# Point(x=1023, y=767)
	# Point(x=0, y=767)
	# Point(x=506, y=0)
	# Point(x=528, y=112)
	# Point(x=574, y=385)
	# Point(x=313, y=332)
	# Point(x=93, y=393)
	# Point(x=172, y=371)

#todo: part-2
pyautogui.displayMousePosition()