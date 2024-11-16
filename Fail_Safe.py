#Import the relevant Modules

import pyautogui
import time

#Fail Safe - Do Not Disable This
pyautogui.FAILSAFE = True

# Example
time.sleep(3)
text = open("text.txt")
for each_line in text:
    pyautogui.write(each_line)
