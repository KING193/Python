# AUTOMATION-3
import pyautogui

pyautogui.click(1158, 300)
pyautogui.typewrite("Hellom I like footballm what do you like?")#todo write

#? Add interval

pyautogui.click(1158, 300)
pyautogui.typewrite("\nHellom I like footballm what do you like?", interval=0.1)#todo write solmochan

# #? Add Keys
pyautogui.typewrite(["\n" ,"b", "c", "left", "left", "a"], interval=0.1)

#goad key
pyautogui.press("F11")
pyautogui.press("alt")

#tow or maany key
pyautogui.hotkey("ctrl", "win", "left", interval=0.2)
pyautogui.hotkey("ctrl", "win", "right", interval=0.2)
pyautogui.hotkey("ctrl", "alt", "left", interval=0.3)
pyautogui.hotkey("ctrl", "alt", "right", interval=0.3)

# #//
print(pyautogui.KEYBOARD_KEYS)
# #//

#* code for joak hack:
pyautogui.typewrite(["win"])
pyautogui.typewrite("cmd")
pyautogui.typewrite(["enter"], interval=0.1)
pyautogui.typewrite("color a & dir/s", interval=0.1)
pyautogui.typewrite(["enter"], interval= 0.1)