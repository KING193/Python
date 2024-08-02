import pyautogui
import time

time.sleep(2)#?What 2s
pyautogui.screenshot("C:\\Users\\DELL\\Desktop\\Programr\\Python\\iS7ee7\\none\\fullscreen.png")#screenshot

coords = pyautogui.locateAllOnScreen("C:\\Users\\DELL\\Desktop\\Programr\\Python\\iS7ee7\\none\\file.png")
for x in coords:
    print(x)# => were file from screenshot
    x , y = list(x)[0:2]

for i in range(2):
    pyautogui.click(x, y)# tow Click file

#COMPLEAT