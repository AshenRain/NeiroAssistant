import time
import numpy as np
import pyscreenshot as ImageGrab
import os
import cv2
import pytesseract


# Путь для подключения tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


filename = 'Image.png'
fl = 1
last_time = time.time()

while(True):
	print(fl)
	if fl == 2:
		cv2.destroyAllWindows()
		break
	
	screen = np.array(ImageGrab.grab(bbox=(0,0,625,402)))
	#screen = np.array(ImageGrab.grab(bbox=(-1920,120,-1287,515))) не работает со вторым экраном (скорее всего из за отрицательных координат)
	print('loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	cv2.imshow('Window vision',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	cv2.imwrite(filename, screen)

	# Подключение фото
	#img = cv2.imread('4-esEJgh_kI.jpg')
	img = cv2.imread('Image.PNG')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	# Будет выведен весь текст с картинки
	config = r'--oem 3 --psm 6'
	print(pytesseract.image_to_string(img, lang='rus+eng', config=tessdata_dir_config))
	data = pytesseract.image_to_data(img, lang='rus+eng', config=tessdata_dir_config)

	# Перебираем данные про текстовые надписи
	for i, el in enumerate(data.splitlines()):
		if i == 0:
			continue

		el = el.split()
		try:
			# Создаем подписи на картинке
			x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
			print(x,y,w,h, el[11])
			cv2.rectangle(img, (x - 5, y - 5), (w + x + 10, h + y + 10), (0, 0, 255), 1)
			#cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
		except IndexError:
			print("Операция была пропущена")

	# Отображаем фото
	cv2.imshow('Result', img)
	cv2.waitKey(0)
	fl = fl + 1
