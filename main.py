import pyscreenshot as ImageGrab
import cv2
import pytesseract
import os
from pynput.keyboard import Key, Controller
from Xlib import display
from time import sleep

cont = False
i = 1
keyboard = Controller()

def getTryStr():
	return '[' + str(i) + '] '

while not cont:
	sleep(3)
	print(getTryStr() + 'Checking for match...')
	data = display.Display().screen().root.query_pointer()._data
	data["root_x"], data["root_y"]
	x = data["root_x"]
	y = data["root_y"]
	print(getTryStr() + 'Mouse position: ' + str(x) + ', ' + str(y))
	print(getTryStr() + 'Taking screenshot...')
	im = ImageGrab.grab(bbox=(x - 512, y - 512, x + 512, y + 512))
	im.save("temp.png")
	print(getTryStr() + 'Took screenshot.')
	print(getTryStr() + 'Starting OCR thread...')
	img = cv2.imread('temp.png')
	text = pytesseract.image_to_string(img)
	modtext = os.linesep.join([s for s in text.splitlines() if s])
	print(getTryStr() + 'OCR thread done.')
	if ("YOUR MATCH IS READY" in text):
		print(getTryStr() + "Ready... pressing space.")
		cont = True
		keyboard.press(' ')
		sleep(0.05)
		keyboard.release(' ')
		print(getTryStr() + "OK.")
	else:
		print(getTryStr() + "Still not ready...")
	os.remove('temp.png')
	i+=1
