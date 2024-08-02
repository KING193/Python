import time

class Click:
    hour = 0
    minute = 0
    
    time_1 = int(input("What hour you need: "))
    time_2 = int(input("What minute you need: "))

    @classmethod
    def week_up(cls):
        if cls.time_1  <= 24 and cls.time_2 <= 60:
    
            while cls.hour != cls.time_1  or cls.minute != cls.time_2:

                cls.minute += 1
                if cls.minute > 60:
                    
                    cls.hour += 1
                    cls.minute = 1  
                time.sleep(0.5)
                print(str(cls.hour) + ":" + str(cls.minute))

            print("It\'s a time week up!")

        else:

            print("Max hour is 24 and max minute is 60")

Click.week_up()