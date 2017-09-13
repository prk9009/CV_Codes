#When we take an image using pin-hole camera, we loose an important information, ie depth of the image. Or how far
#is each point in the image from the camera because it is a 3D-to-2D conversion. So it is an important question whether
#we can find the depth information using these cameras. And the answer is to use more than one camera.

#the place where we use kinect
#everything explained in notes (for working)

#So first we need to find as many possible matches between two images to find the fundamental matrix. For this, we
#use SIFT descriptors with FLANN based matcher and ratio test.



import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread('myleft.jpg',0) #queryimage # left image
img2 = cv2.imread('myright.jpg',0) #trainimage # right image
sift = cv2.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
good = []
pts1 = []
pts2 = []
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
	if m.distance < 0.8*n.distance:
		good.append(m)
		pts2.append(kp2[m.trainIdx].pt)
		pts1.append(kp1[m.queryIdx].pt)

#Now we have the list of best matches from both the images. Let’s find the Fundamental Matrix.

pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)
# We select only inlier points
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]


#Epilines corresponding to the points in first image is drawn on second image. So mentioning of correct images
#are important here. We get an array of lines. So we define a new function to draw these lines on the images.


def drawlines(img1,img2,lines,pts1,pts2):
	''' img1 - image on which we draw the epilines for the points in img2
	lines - corresponding epilines '''
	r,c = img1.shape
	img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
	img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
	for r,pt1,pt2 in zip(lines,pts1,pts2):
		color = tuple(np.random.randint(0,255,3).tolist())
		x0,y0 = map(int, [0, -r[2]/r[1] ])
		x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
		img1 = cv2.line(img1, (x0,y0), (x1,y1), color,1)
		img1 = cv2.circle(img1,tuple(pt1),5,color,-1)
		img2 = cv2.circle(img2,tuple(pt2),5,color,-1)
	return img1,img2

#Now we find the epilines in both the images and draw them.

# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2,F)
lines1 = lines1.reshape(-1,3)
img5,img6 = drawlines(img1,img2,lines1,pts1,pts2)
# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2,img1,lines2,pts2,pts1)
plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img3)
plt.show()

#For better results, images with good resolution and many non-planar points should be used.


##
##
#Depth Map from Stereo Images

#disparity = x − x ′ =Bf/Z

#x and x ′ are the distance between points in image plane corresponding to the scene point 3D and their camera center.
#B is the distance between two cameras (which we know) and f is the focal length of camera (already known).


import numpy as np
import cv2
from matplotlib import pyplot as plt
imgL = cv2.imread('tsukuba_l.png',0)
imgR = cv2.imread('tsukuba_r.png',0)
stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()





















