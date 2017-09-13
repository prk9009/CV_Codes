# diff b/w shithomas, harris and sift is that it is scale invariant

#1. Scale-space Extrema Detection
#LoG acts as a blob detector which detects
#blobs in various sizes due to change in σ. In short, σ acts as a scaling parameter
#with low σ gives high value for small corner while guassian kernel with high σ fits well for larger corner. So,
#we can find the local maxima across the scale and space which gives us a list of (x, y, σ) values which means there is
#a potential keypoint at (x,y) at σ scale.
#SIFT algorithm uses Difference of Gaussians which is an approximation of LoG.
#Difference of Gaussian is obtained as the difference of Gaussian blurring of an image with two different σ, let it be σ
#and kσ. This process is done for different octaves of the image in Gaussian Pyramid.
#Once this DoG are found, images are searched for local extrema over scale and space. For eg, one pixel in an image is
#compared with its 8 neighbours as well as 9 pixels in next scale and 9 pixels in previous scales. If it is a local extrema,
#it is a potential keypoint. It basically means that keypoint is best represented in that scale.

#2. Keypoint Localization
#a 2x2 Hessian matrix (H) to compute the pricipal curvature. We know from Harris corner
#detector that for edges, one eigen value is larger than the other. So here they used a simple function,
#If this ratio is greater than a threshold, called edgeThreshold in OpenCV, that keypoint is discarded. It is given as 10 in paper.
#So it eliminates any low-contrast keypoints and edge keypoints and what remains is strong interest points.

#3. Orientation Assignment
#The highest peak in the histogram is taken and any peak above 80% of it is also considered to calculate the orientation.
# It creates keypoints with same location and scale, but different directions. It contribute to stability of matching.


#4. Keypoint Descriptor
#A 16x16 neighbourhood around the keypoint is taken. It is devided into 16
#sub-blocks of 4x4 size. For each sub-block, 8 bin orientation histogram is created. So a total of 128 bin values are
#available. It is represented as a vector to form keypoint descriptor.

#5. Keypoint Matching
#Keypoints between two images are matched by identifying their nearest neighbours. But in some cases, the second
#closest-match may be very near to the first. It may happen due to noise or some other reasons. In that case, ratio of
#closest-distance to second-closest distance is taken. If it is greater than 0.8, they are rejected. It eliminaters around
#90% of false matches

import cv2
import numpy as np
img = cv2.imread('home.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp)
cv2.imwrite('sift_keypoints.jpg',img)

#sift.detect() function finds the keypoint in the images. You can pass a mask if you want to search only a part of
#image. Each keypoint is a special structure which has many attributes like its (x,y) coordinates, size of the meaningful
#neighbourhood, angle which specifies its orientation, response that specifies strength of keypoints etc.

#v2.drawKeyPoints() function which draws the small circles on the locations of keypoints. If
#you pass a flag, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS to it, it will draw a circle with size
#of keypoint and it will even show its orientation.

img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints.jpg',img)

#1. Since you already found keypoints, you can call sift.compute() which computes the descriptors from the key-
#points we have found. Eg: kp,des = sift.compute(gray,kp)
#2. If you didn’t find keypoints, directly find keypoints and descriptors in a single step with the function,
#sift.detectAndCompute().

sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray,None)

#Here kp will be a list of keypoints and des is a numpy array of shape N umber_of _Keypoints × 128.
#Now we see how to match these feature points






















































































