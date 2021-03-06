#we can use a function from calib3d module, ie cv2.findHomography(). If we pass the set of points from both
#the images, it will find the perpective transformation of that object. Then we can use cv2.perspectiveTransform() to
#find the object. It needs atleast four correct points to find the transformation.

#RANSAC So good matches which provide
#correct estimation are called inliers and remaining are called outliers. cv2.findHomography() returns a mask which
#specifies the inlier and outlier points

#First, as usual, let’s find SIFT features in images and apply the ratio test to find the best matches.

import numpy as np
import cv2
from matplotlib import pyplot as plt
MIN_MATCH_COUNT = 10
img1 = cv2.imread('box.png',0)
# queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage
# Initiate SIFT detector
sift = cv2.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
	if m.distance < 0.7*n.distance:
		good.append(m)


#we set a condition that atleast 10 matches (defined by MIN_MATCH_COUNT) are to be there to find the object.
#Otherwise simply show a message saying not enough matches are present.
#we extract the locations of matched keypoints in both the images. They are passed to
#find the perpective transformation. Once we get this 3x3 transformation matrix, we use it to transform the corners of
#queryImage to corresponding points in trainImage.

if len(good)>MIN_MATCH_COUNT:
	src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
	dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
	M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
	matchesMask = mask.ravel().tolist()
	h,w = img1.shape
	pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
	dst = cv2.perspectiveTransform(pts,M)
	img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
else:
	print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
	matchesMask = None

#Finally we draw our inliers (if successfully found the object) or matching keypoints (if failed).

draw_params = dict(matchColor = (0,255,0),  color singlePointColor = None, matchesMask = matchesMask,  flags = 2)# draw matches in green # draw only inliers
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
plt.imshow(img3, 'gray'),plt.show()































