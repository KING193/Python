# AUTOMATION
import pyautogui
# pip install pyautogui

#tariqah ma3refah mawqe3 lemos 3alla sash:
pyautogui.position()# => Point(x=878, y=307)

#ma3refah mosa7aht sash:
pyautogui.size()# => Size(width=1024, height=768)

#7afat leqaim:
width, height = pyautogui.size()
print(width)# => 1024
print(height)# => 768

#ta7arik lemos:
pyautogui.move(1000, 1000)

#Pals duration:
pyautogui.move(1000, 1000, duration=2)# ta7arik lemos bebot

#ta7arik lemos 7asab mosa7aht sash:
pyautogui.moveTo(0, 0, duration=3)# ta7arik mon 0 ela 1024 and mon 0 ela 768
pyautogui.moveTo(-1000, -400, duration=3)# ta7arik 3aks

#daghat ba lemos:
pyautogui.position()# Point(x=844, y=55)
pyautogui.click(844, 55)# daghat ba lemos 3alla mawqe3 844, 55

#daghat moratin ba lemos:
pyautogui.doubleClick(93, 538)# daghat moratin ba lemos 3alla mawqe3 93, 538

#daghat leftClick ba lemos:
pyautogui.leftClick(93, 538)# daghat leftClick ba lemos 3alla mawqe3 93, 538

#daghat middleClick ba lemos:
pyautogui.middleClick(93, 538)# daghat middleClick ba lemos 3alla mawqe3 93, 538

#daghat rightClick ba lemos:
pyautogui.rightClick(93, 538)# daghat rightClick ba lemos 3alla mawqe3 93, 538