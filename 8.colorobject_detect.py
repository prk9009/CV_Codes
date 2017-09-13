import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
#must be done in hsv onlly and to find hsv value jut type np.array([])value of the color and just cvtColor o hsv as above and check its color
	lower_blue = np.array([150,150,150])
	upper_blue = np.array([255,255,255])
# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image

	res = cv2.bitwise_and(frame,frame, mask= mask)
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
