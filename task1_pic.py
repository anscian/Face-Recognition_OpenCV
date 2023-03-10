import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv.imread('test.jpg')

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#faces = face_cascade.detectMultiScale(gray, 1.1, 10)

faces = face_cascade.detectMultiScale(img, 1.1, 10)

for (x, y, w, h) in faces:
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
cv.imshow('img', img)
cv.waitKey(0)
