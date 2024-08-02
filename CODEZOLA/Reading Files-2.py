'''
					|r  r+   w  w+   a  a+
--------------------|----------------------
read 				|+  +       +       +
write 				|   +    +  +    +  +
create 				|        +  +    +  +
truncate			|        +  +
position at start   |+  +    +  +
position at end 	|                +  +

'''

workers_file = open("workers-2", "a")
#edafat nas ela lemalf
workers_file.write("hunter x hunter - Sniper")# => Add to file
workers_file.write("\nhunter x hunter - Sniper")# => Add to file in new line
workers_file.close()

#a+:
workers_file = open("workers-2", "a+")
workers_file.write("hunter x hunter - Sniper")# => Add to file
workers_file.write("\nhunter x hunter - Sniper")# => Add to file in new line
workers_file.close()

#w:
workers_file = open("workers-2", "w")
workers_file.write("hunter x hunter - Sniper")# => Add to file
workers_file.write("\nhunter x hunter - Sniper")# => Add to file in new line
workers_file.close()

workers_file = open("workers-2", "w")
#eadfaht ekthar mon satr mar wa7d
list_of_phrases = ["\nthis is a first line", "\nthis is a second line", "\nthis is a third line",]
workers_file.writelines(list_of_phrases)# => 
										# => this is a first line
										# => this is a second line
										# => this is a third line
workers_file.close()


#w+:
workers_file = open("workers-2", "w+")
workers_file.write("hunter x hunter - Sniper")# => Add to file
workers_file.write("\nhunter x hunter - Sniper")# => Add to file in new line
workers_file.close()

#Html file:
workers_file = open("html_python.html", "w")
workers_file.write("<p>this is a paragraph</p>")# => Add to file
workers_file.close()
