#, cv2.goodFeaturesToTrack(). It finds N strongest corners in the image by Shi-Tomasi method
#(or Harris Corner Detection, if you specify it). As usual, image should be a grayscale image. Then you specify
#number of corners you want to find. Then you specify the quality level, which is a value between 0-1, which denotes
#the minimum quality of corner below which everyone is rejected. Then we provide the minimum euclidean distance
#between corners detected. Then function takes first strongest corner,
#throws away all the nearby corners in the range of minimum distance and returns N strongest corners.


import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('simple.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
x,y = i.ravel()
cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()


































