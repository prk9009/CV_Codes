#Optical Flow


#• Structure from Motion
#• Video Compression
#• Video Stabilization ...




#Optical flow works on several assumptions:
#1. The pixel intensities of an object do not change between consecutive frames
#2. Neighbouring pixels have similar motion.

#Consider a pixel I(x, y, t) in first frame It moves by distance (dx, dy) in next frame taken after dt time. So since those pixels
#are the same and intensity does not change, we can say,
#I(x, y, t) = I(x + dx, y + dy, t + dt)
#f x u + f y v + f t = 0

#WE GET OPTICAL FLOW EQUATION

#In it, we can find f x and f y , they are image gradients. Similarly f t
#is the gradient along time. But (u, v) is unknown. We cannot solve this one equation with two unknown variables. So
#several methods are provided to solve this problem and one of them is Lucas-Kanade

#Lucas-Kanade method

#we give some points to track, we receive the optical flow vectors of those
#points. But again there are some problems. Until now, we were dealing with small motions. So it fails when there
#is large motion. So again we go for pyramids. When we go up in the pyramid, small motions are removed and large
#motions becomes small motions. So applying Lucas-Kanade there, we get optical flow along with the scale.

#Lucas-Kanade Optical Flow in OpenCV

#cv2.calcOpticalFlowPyrLK(). Here, we create a simple application
#which tracks some points in a video. To decide the points, we use cv2.goodFeaturesToTrack().

#then we iteratively track those points using Lucas-Kanade optical
#flow. For the function cv2.calcOpticalFlowPyrLK() we pass the previous frame, previous points and next frame.
#It returns next points along with some status numbers which has a value of 1 if next point is found, else zero. We
#iteratively pass these next points as previous points in next step. See the code below:

import numpy as np
import cv2
cap = cv2.VideoCapture('slow.flv')
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,qualityLevel = 0.3,minDistance = 7,blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(100,3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
	ret,frame = cap.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# calculate optical flow
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
# Select good points
	good_new = p1[st==1]
	good_old = p0[st==1]
	# draw the tracks
	for i,(new,old) in enumerate(zip(good_new,good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
		frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
	img = cv2.add(frame,mask)
	cv2.imshow('frame',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
# Now update the previous frame and previous points
	old_gray = frame_gray.copy()
	p0 = good_new.reshape(-1,1,2)
cv2.destroyAllWindows()
cap.release()

#This code doesn’t check how correct are the next keypoints. So even if any feature point disappears in image, there
#is a chance that optical flow finds the next point which may look close to it. So actually for a robust tracking, corner points should be detected in particular intervals
#It also run a backward-check of the optical flow points got to select only good ones.


#“Two-Frame Motion Estimation Based on Polynomial Expansion”

#We get a 2-channel array with optical flow vectors, (u, v). We find their magnitude and direction. We color code 
#the result for better visualization. Direction corresponds to Hue value of the image. Magnitude corresponds to Value plane

import cv2
import numpy as np
cap = cv2.VideoCapture("output.avi")
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
	ret, frame2 = cap.read()
	next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
	flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
	hsv[...,0] = ang*180/np.pi/2
	hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
	rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
	cv2.imshow('frame2',rgb)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
	elif k == ord('s'):
		cv2.imwrite('opticalfb.png',frame2)
		cv2.imwrite('opticalhsv.png',rgb)
		prvs = next
cap.release()
cv2.destroyAllWindows()



































