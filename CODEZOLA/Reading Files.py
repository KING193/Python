open("workers", "r")# r w a
# fata7 lemalf waba3d dalk esm lemalf w no3 le3amaly

#read mod:

# ta7aqeq mon lemalf
workers_file = open("workers", "r")
print(workers_file.readable())# => True
workers_file.close()

# yoqaraha lemalf
workers_file = open("workers", "r")
print(workers_file.read())#Islam - Programming Instructor; Pikachu - Frontend Developer; Subzero - Backend Developer; Sonic - Business Analyst; Tails - Data Analyst; Eren - Data Engineer
workers_file.close()

# yoqaraha satr lol faqat
workers_file = open("workers", "r")
print(workers_file.readline())# => Islam - Programming Instructor
print(workers_file.readline())# => Pikachu - Frontend Developer
print(workers_file.readline())# => Subzero - Backend Developer
workers_file.close()

# yoqaraha lemalf kamal fy list
workers_file = open("workers", "r")
print(workers_file.readlines())# => ['Islam - Programming Instructor \n', 'Pikachu - Frontend Developer\n', 'Subzero - Backend Developer\n', 'Sonic - Business Analyst\n', 'Tails - Data Analyst\n', 'Eren - Data Engineer']
workers_file.close()

workers_file = open("workers", "r")
print(workers_file.readlines()[0])# => Islam - Programming Instructor
#print(workers_file.readlines()[5]) #IndexError: list index out of range
workers_file.close()

workers_file = open("workers", "r")
print(workers_file.readlines()[3])# => Sonic - Business Analyst
workers_file.close()

#Pals For Loop:
workers_file = open("workers", "r")
for worker in workers_file.readlines():
	print(worker)# Islam - Programming Instructor

				 # Pikachu - Frontend Developer

				 # Subzero - Backend Developer

				 # Sonic - Business Analyst

				 # Tails - Data Analyst

				 # Eren - Data Engineer

workers_file.close()

#Pals is cool:
workers_file = open("workers", "r")
for worker in workers_file.readlines():
	print(worker+ " is cool")# Islam - Programming Instructor
							 #  is cool
							 # Pikachu - Frontend Developer
							 #  is cool
							 # Subzero - Backend Developer
							 #  is cool
							 # Sonic - Business Analyst
							 #  is cool
							 # Tails - Data Analyst
							 #  is cool
							 # Eren - Data Engineer is cool

workers_file.close()

input("run")


#write mod:
#workers_file = open("workers", "w")
# ta7aqeq mon lemalf
#print(workers_file.readable())# => False
#workers_file.close()