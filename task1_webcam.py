import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while 1:
	_, img = cap.read()
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.1, 1)
	
	for (x, y, w, h) in faces:
		cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	cv.imshow('img', img)
	key_pressed = cv.waitKey(5)
	if key_pressed == 27:
		break
		
cap.release()
