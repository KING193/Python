import random

cm_in_meter = 100
meter_in_km = 1000
pink_floyd = ["roger waters", "david qilmour", "syd barett"]

def get_file_ext(filename):
	return filename[filename.index(".") + 1:]

def roll_dice(num):
	return random.randint(1, num)