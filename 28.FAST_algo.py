#Feature Detection using FAST
#1. Select a pixel p in the image which is to be identified as an interest point or not. Let its intensity be I p .
#2. Select appropriate threshold value t.
#3. Consider a circle of 16 pixels around the pixel under test
#4. Now the pixel p is a corner if there exists a set of n contiguous pixels in the circle (of 16 pixels) which are all
#brighter than I p + t, or all darker than I p t. (Shown as white dash lines in the above image). n was chosen to be 12.
#5.This test examines only the four
#pixels at 1, 9, 5 and 13 (First 1 and 9 are tested if they are too brighter or darker. If so, then checks 5 and 13).
#If p is a corner, then at least three of these must all be brighter than I p + t or darker than I p t. If neither of
#these is the case, then p cannot be a corner


#weaknesses:
#• It does not reject as many candidates for n < 12.
#• The choice of pixels is not optimal because its efficiency depends #on ordering of the questions and distri-
#bution of corner appearances.
#• Results of high-speed tests are thrown away.
#• Multiple features are detected adjacent to one another.
#First 3 points are addressed with a machine learning approach. Last one is addressed using non-maximal suppression.


#Machine Learning a Corner Detector
#1. Select a set of images for training (preferably from the target application domain)
#2. Run FAST algorithm in every images to find feature points.
#3. For every feature point, store the 16 pixels around it as a vector. Do it for all the images to get feature vector P .
#4. Each pixel (say x) in these 16 pixels can have one of the following three states:
#5. Depending on these states, the feature vector P is subdivided into 3 subsets, P d , P s , P b .
#6. Define a new boolean variable, K p , which is true if p is a corner and false otherwise.
#7. Use the ID3 algorithm (decision tree classifier) to query each subset using the variable K p for the knowledge
#about the true class. It selects the x which yields the most information about whether the candidate pixel is a
#corner, measured by the entropy of K p .
#8. This is recursively applied to all the subsets until its entropy is zero.
#9. The decision tree so created is used for fast detection in other images.

#Non-maximal Suppression
#Detecting multiple interest points in adjacent locations is another problem. It is solved by using Non-maximum
#Suppression.
#1. Compute a score function, V for all the detected feature points. V is the sum of absolute difference between p
#and 16 surrounding pixels values.
#2. Consider two adjacent keypoints and compute their V values.
#3. Discard the one with lower V value.

##
##
#For the neighborhood, three flags are defined, cv2.FAST_FEATURE_DETECTOR_TYPE_5_8, cv2.
#FAST_FEATURE_DETECTOR_TYPE_7_12 and cv2.FAST_FEATURE_DETECTOR_TYPE_9_16. Below is a
#simple code on how to detect and draw the FAST feature points.

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('simple.jpg',0)
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
# Print all default params
print "Threshold: ", fast.getInt('threshold')
print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
print "neighborhood: ", fast.getInt('type')
print "Total Keypoints with nonmaxSuppression: ", len(kp)
cv2.imwrite('fast_true.png',img2)
# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)
print "Total Keypoints without nonmaxSuppression: ", len(kp)
img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))
cv2.imwrite('fast_false.png',img3)
























