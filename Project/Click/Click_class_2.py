import time

class Click:
    hour = 0
    minute = 0

    def __init__(self, time_1, time_2):
        self.time_1 = time_1
        self.time_2 = time_2

    def week_up(self):
        if self.time_1  <= 24 and self.time_2 <= 60:
    
            while Click.hour != self.time_1  or Click.minute != self.time_2:

                Click.minute += 1
                if Click.minute > 60:
                    
                    Click.hour += 1
                    Click.minute = 1  
                time.sleep(0.5)
                print(str(Click.hour) + ":" + str(Click.minute))

            print("It\'s a time week up!")

        else:

            print("Max hour is 24 and max minute is 60")

click_1 = Click(3, 33)
click_1.week_up()