import time

x = 1

hour = 0
minute = 0

while x == 1:

    try:

        time_1 = int(input("What hour you need: "))
        time_2 = int(input("What minute you need: "))

        if time_1 <= 24 and time_2 <= 60:
    
            while hour != time_1 or minute != time_2:

                minute += 1
                if minute > 60:
                    
                    hour += 1
                    minute = 1
                time.sleep(0.5)
                print(str(hour) + ":" + str(minute))

            print("It\'s a time week up!")
            x = 0

        else:

            print("Max hour is 24 and max minute is 60")
        
    except:
        print("Enter Number")