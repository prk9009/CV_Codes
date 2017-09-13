#BackgroundSubtractorMOG

#It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.

#It uses a method to model each background pixel by a mixture of K Gaussian distributions (K
#= 3 to 5). The weights of the mixture represent the time proportions that those colours stay in the scene. The probable
#background colours are the ones which stay longer and more static

#we need to create a background object using the function, cv2.createBackgroundSubtractorMOG().
#It has some optional parameters like length of history, number of gaussian mixtures, threshold etc. It is all set to some
#default values. Then inside the video loop, use backgroundsubtractor.apply() method to get the foreground mask.


import numpy as np
import cv2
cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG()
while(1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()

#BackgroundSubtractorMOG2

#, we have to create a background subtractor object. Here, you have an option of selecting whether
#shadow to be detected or not. If detectShadows = True (which is so by default), it detects and marks shadows,
#but decreases the speed. Shadows will be marked in gray color

import numpy as np
import cv2
cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()


#BackgroundSubtractorGMG

#This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation.

#It uses first few (120 by default) frames for background modelling. It employs probabilistic foreground segmentation
#algorithm that identifies possible foreground objects using Bayesian inference. The estimates are adaptive; newer
#observations are more heavily weighted than old observations to accommodate variable illumination. Several morpho-
#logical filtering operations like closing and opening are done to remove unwanted noise. You will get a black window
#during first few frames.


import numpy as np
import cv2
cap = cv2.VideoCapture('vtest.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorGMG()
while(1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()




























