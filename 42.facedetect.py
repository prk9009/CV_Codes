#Haar-cascade Detection in OpenCV
#OpenCV comes with a trainer as well as detector. If you want to train your own classifier for any object like car, planes
#etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.
#Here we will deal with detection. OpenCV already contains many pre-trained classifiers for face, eyes, smile etc.
#Those XML files are stored in opencv/data/haarcascades/ folder. Let’s create face and eye detector with OpenCV.


import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('sachin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once
#we get these locations, we can create a ROI for the face and apply eye detection on this ROI


faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()









