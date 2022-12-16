import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture('crowd.mp4')

status, img = cap.read()
while status:
	#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	#faces = face_cascade.detectMultiScale(img, 1.1, 10)

	print((status, img))
	
	faces = face_cascade.detectMultiScale(img, 1.4, 10) # increased scale factor to have normal fps for the result video
	
	for (x, y, w, h) in faces:
		cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	cv.imshow('img', img)
	
	k = cv.waitKey(3)
	if k == 27:
		break
	
	status, img = cap.read()

cap.release()
