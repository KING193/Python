coordinates = (23, 45)
print(coordinates)#atab3 lea (23, 45)

print(coordinates[1])#atab3 lea 45
print(coordinates[0])#atab3 lea 23

Food_in_Morocco = [("Wheat","Fruit","Banunas"), ("Cow","Sheep","Fishs")]#?List dakhal Tuples 
print(Food_in_Morocco)#atab3 lea [("Wheat","Fruit","Banunas"), ("Cow","Sheep","Fishs")]



#*Error:
coordinates[0] = 66
#todo print(coordinates)#!Error: 'tuple' object does not support item assignment
Food_in_Morocco[1][0] = "Bread"
#todo print(Food_in_Morocco)#!Error: 'tuple' object does not support item assignment