friends = [1, "codezille", True, False, [1,"mohamed"]]
print(friends)

friends1 = [2, "code", True, False, [2,"simo"]]
print(friends1[0])# 0 = 2
print(friends1[4])#4 = [2,'simo']

python = ["example", "zille", "python", "programing"]
print(python[-1])#print programing
print(python[-2])#print python


COLON = [True, True, 75, "colon"]
print(COLON[1:3])#no print 3(clon) is print 2(75)

python1 = ["bin", "venv", "lops", "pop", "termux"]
print(python1[0:3])#From bin to lops, 0 = bin, 3 = lops

apartment = ["armchair", "bed", "picture", "coffee taple"]
apartment[0] = "sofa"#armchair => sofa
print(apartment[0])

apartment2 = ["dresser", "lamp", "boohcase", "sofa"]
apartment2[1] = "window"#lamp => window
print(apartment2)


print(python[-5])#Error: list index out of range