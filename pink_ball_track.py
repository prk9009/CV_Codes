import cv2
import numpy as np
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
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

	#cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
	_,contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) > 0:
		#print 1
		cnt = contours[0]
		M = cv2.moments(cnt)
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		print center
		radius = int(radius)
		#rect = cv2.minAreaRect(cnt)
		#box = cv2.boxPoints(rect)
		#box = np.int0(box)
		#im = cv2.drawContours(frame,[box],0,(0,0,0),2)
		frame = cv2.circle(frame,center,radius,(0,0,0),2)
		cv2.imshow('frame',frame)
		out.write(frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
