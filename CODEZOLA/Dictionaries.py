convert_month = {
	"jan" : "january",
	"feb" : "febraury",
	"mar" : "march"
}

print(convert_month["mar"])#print march
print(convert_month["jan"])#print january
print(convert_month["feb"])#print febraury

#Pals get:
print(convert_month.get("jan"))#jan => january
print(convert_month.get("lol"))#None is "lol" not key

print(convert_month.get("fish", "the value does not exist"))#print => the value does not exist lan "fish" not key badl None
print(convert_month.get("mar", "tab3an ana hena momken ay 7aga"))#print march lan mat is key

scp = {
	1 : "scp-049",
	2 : "scp-001",
	3 : 6,
	4 : True,
	6 : ["scp-212", 6, "scp-000"]
}

print(scp.get(2, "the value does not exist"))#print scp-001
print(scp.get(6, "the value does not exist"))#print ["scp-212", 6, "scp-000"]

print(scp[4])##
print(scp.get(1,"not is 1 key"))#tab3 lay "scp-049"

#Error:
convert_month_2 = {
	"jan" : "january",
	"jan" : "febraury",
	"mar" : "march"
}
print(convert_month_2["jan"])#print febrauty not january

convert_month_3 = {
	"jan" : "january",
	"jan" : "febraury",
	"jan" : "march"
}
print(convert_month_3["jan"])#print march
#Dictionary contains duplicate keys 'jan'

print(convert_month["Mar"])#not Mar is mar