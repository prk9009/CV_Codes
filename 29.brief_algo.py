#BRIEF comes into picture at this moment. It provides a shortcut to find the binary strings directly without finding
#descriptors. It takes smoothened image patch and selects a set of n d (x,y) location pairs in an unique way
#Then some pixel intensity comparisons are done on these location pairs. For eg, let first location pairs be p and
#q. If I(p) < I(q), then its result is 1, else it is 0. This is applied for all the n d location pairs to get a n d -dimensional
#bitstring. This n d can be 128, 256 or 512.
#So once you get this, you can use Hamming Distance to match these descriptors

#BRIEF is a feature descriptor, it doesn’t provide any method to find the features. So you
#will have to use any other feature detectors like SIFT, SURF, CenSurE etc.


import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('simple.jpg',0)
# Initiate STAR detector
star = cv2.FeatureDetector_create("STAR")
# Initiate BRIEF extractor
brief = cv2.DescriptorExtractor_create("BRIEF")
# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print brief.getInt('bytes')
print des.shape

#The function brief.getInt('bytes') gives the n d size used in bytes. By default it is 32.


















