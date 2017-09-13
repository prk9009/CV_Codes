#check online for notes on ORB 2011 

#It has a number of optional parameters. Most useful ones are nFeatures which denotes maximum number of features
#to be retained (by default 500), scoreType which denotes whether Harris score or FAST score to rank the features
#(by default, Harris score) etc. Another parameter, WTA_K decides number of points that produce each element of
#the oriented BRIEF descriptor. By default it is two, ie selects two points at a time. In that case, for matching,
#NORM_HAMMING distance is used. If WTA_K is 3 or 4, which takes 3 or 4 points to produce BRIEF descriptor, then
#matching distance is defined by NORM_HAMMING2.

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('simple.jpg',0)
# Initiate STAR detector
orb = cv2.ORB()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()





