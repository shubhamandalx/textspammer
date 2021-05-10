import pyautogui
import time

time.sleep(5)
fi = open("baby.txt","r")
#fi = "hello"
for each in fi:
	pyautogui.typewrite(each)
	pyautogui.press("enter")
