text = "codezilla"
print(text)

#Pals lower:
text = "COdezilla"
print(text.lower())#print + text.lower => codezilla

#Pals upper:
text = "COdezilla"
print(text.upper())#print + text.upper => CODEZILLA

#Pals isupper:
text = "COdezilla"
print(text.isupper())#print + text.isupper => False

#Pals islower:
text = "COdezilla"
print(text.islower())#print + text.islower => False

#Pals lower and islower:
text = "COdezilla"
print(text.lower().islower())#print + text.lower + text.islower => True

#Pals lower and isupper:
text = "COdezilla"
print(text.lower().isupper())#print + text.lower + text.isupper => False

#len:
text = "COdezilla"
print(len(text))#print + len(text) => 9
print(len("dog"))#print + len(dog) => 3

#ma3refah makan el7araf:
text = "codezilla"
       #012345678
print(text[0])#text[0] => print(c)
print(text[4])#text[4] => print(z)

first_name = "hesham"
last_name = "islam"

print(first_name[0],last_name[0])#print first_name[0] + last_name[0] => h i

text = "codezilla"

print(text.index("c"))#print text + index("c") => 0
print(text.index("z"))#print text + index("z") => 4
#print(text.index("y")) Error:substing not found

print(text.index("zilla"))#print text + index("zilla") => 4

#replace:
text = "codezilla"

print(text.replace("code","mode"))#print text + replace => modezilla
print(text.replace("code","k"))#print text + replace => kzilla
print(text.replace("zilla","k"))#print text + replace => codek

print(text.replace("codezilla"),"python")#print text + replace => python
