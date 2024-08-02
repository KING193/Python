Housing_1 = ["living-room", "stairs", "dining-room", "terrace", "kitchen", "garage", "yard"]
Adjectives_1 = ["good", "nice", "bad"]

Housing_2 = ["balcony", "bed-room", "hall", "closet", "bath-room", "outside"]
Punctuation = ["full stop", "comma", "question mark", "exclamation mark"]

print(Housing_1,Housing_2)#Pals
Adjectives_1 += Punctuation#Pals
Housing_2 = Housing_2 + Punctuation#Pals

print(Adjectives_1)

#finchan extend:
Housing_2.extend(Adjectives_1)#Add Adjectives_1 on Housing_2
print(Housing_2)

#finchan append:
Adjectives_1.append("Fak")#Add Fak to Adjectives_1
print(Adjectives_1)

Adjectives_1.append([1,2,3,4])#Add List[1,2,3,4] to Adjectives_1
print(Adjectives_1)

#finchan insert:
Punctuation.insert(2,"html")#Add "html" in adris(2) after "comma"

#finchan remove:
Housing_1.remove("living-room")#Delete "living-room" from Housing_1
print(Housing_1)

Shopping = ["CDs", "books", "toys", "Cakes"]
Shopping.remove("css")#Error: list.remove(x): x not in list,x="css"
#print(Shopping)

#finchan clear:
Shopping.clear()#Delete All => Shopping[]
print(Shopping)

#finchan pop:
Shopping.pop()#Delete END => remove "Cakes"
print(Shopping)

storage = Shopping.pop()#Stor END(Cakes) in storage
print(storage)

Numbers = [423,76,221,9,45,0,2,4,65,23]

#finchan index:
Numbers.index(0)#Search for Makan Value(0)
print(Numbers)#print Makan valyo => 5
#index or:
print(Numbers.index(221))#Search for Makan Value(221) and print Makan valyo => 2
#eda lem yokan Value mawogod:
Numbers.index(999)
print(Numbers)#Error: 999 is not in list