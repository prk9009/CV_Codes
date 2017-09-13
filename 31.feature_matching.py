#BF matcher, first we have to create the BFMatcher object using cv2.BFMatcher(). It takes two optional params.
#First one is normType. It specifies the distance measurement to be used. By default, it is cv2.NORM_L2. It is good
#for SIFT, SURF etc (cv2.NORM_L1 is also there). For binary string based descriptors like ORB, BRIEF, BRISK etc,
#cv2.NORM_HAMMING should be used, which used Hamming distance as measurement. If ORB is using VTA_K ==
#3 or 4, cv2.NORM_HAMMING2 should be used.

#Second param is boolean variable, crossCheck which is false by default. If it is true, Matcher returns only those
#matches with value (i,j) such that i-th descriptor in set A has j-th descriptor in set B as the best match and vice-versa.

#Once it is created, two important methods are BFMatcher.match() and BFMatcher.knnMatch(). First one returns the
#best match. Second method returns k best matches where k is specified by the user

#we used cv2.drawKeypoints() to draw keypoints, cv2.drawMatches() helps us to draw the matches. It stacks
#two images horizontally and draw lines from first image to second image showing best matches. There is also
#cv2.drawMatchesKnn which draws all the k best matches. If k=2, it will draw two match-lines for each keypoint.


import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('box.png',0)
# queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage
# Initiate SIFT detector
orb = cv2.ORB()
# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#Next we create a BFMatcher object with distance measurement cv2.NORM_HAMMING (since we are using ORB) and
#crossCheck is switched on for better results. Then we use Matcher.match() method to get the best matches in two images.

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)
plt.imshow(img3),plt.show()


#The result of matches = bf.match(des1,des2) line is a list of DMatch objects. This DMatch object has following attributes:
#• DMatch.distance - Distance between descriptors. The lower, the better it is.
#• DMatch.trainIdx - Index of the descriptor in train descriptors
#• DMatch.queryIdx - Index of the descriptor in query descriptors
#• DMatch.imgIdx - Index of the train image.

#This time, we will use BFMatcher.knnMatch() to get k best matches


import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('box.png',0)
# queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage
# Initiate SIFT detector
sift = cv2.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m,n in matches:
	if m.distance < 0.75*n.distance:
		good.append([m])
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)
plt.imshow(img3),plt.show()


























