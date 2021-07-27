import time
import numpy as np
import pyscreenshot as ImageGrab
import os
import cv2
import pytesseract

filename = 'Image.png'
x = 1
last_time = time.time()

while(True):
	screen = np.array(ImageGrab.grab(bbox=(0,0,625,402)))
	#screen = np.array(ImageGrab.grab(bbox=(-1920,120,-1287,515))) не работает со вторым играном (скорее всего из за отрицательных координат)
	print('loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	cv2.imwrite(filename, screen)
	x = x + 1
	print(x)
	if x == 2:
		cv2.destroyAllWindows()
		break