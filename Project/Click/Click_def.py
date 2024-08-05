import time

def click(time_1, time_2):
    hour = 0
    minute = 0

    if time_1 <= 24 and time_2 <= 60:
    
            while hour != time_1 or minute != time_2:

                minute += 1
                if minute > 60:
                    
                    hour += 1
                    minute = 1  
                time.sleep(0.5)
                print(str(hour) + ":" + str(minute))

            print("It\'s a time week up!")

    else:

        print("Max hour is 24 and max minute is 60")

quest = input("ON or OFF click: ") 
quest = quest.lower()

while quest == "on":

    print("ON click!")

    quest_1 = int(input("What hour you need: "))
    quest_2 = int(input("What minute you need: "))

    click(quest_1, quest_2)

    quest = input("ON or OFF click: ") 

if quest == "off":
    print("OFF click!")