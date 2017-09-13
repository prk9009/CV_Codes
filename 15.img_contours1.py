#Contours

#Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color
#or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

#For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
#findContours function modifies the source image. So if you want source image even after finding contours,
#already store it to some other variables.
#In OpenCV, finding contours is like finding white object from black background. So remember, object to be
#found should be white and background should be black.

import numpy as np
import cv2
im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#there are three arguments in cv2.findContours(), source, contour retrieval mode, third is contour approximation method.
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
#It can also be used to draw any shape provided you have its boundary points
#first argument is source image, second argument is the contours which should be passed
#as a Python list, third argument is index of contours To draw all contours,
#pass -1) and remaining arguments are color, thickness etc

#M1:img = cv2.drawContours(img, contours, 3, (0,255,0), 3)
#M2:
#cnt = contours[4]
#img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

#in the long run M2 is more useful, but both are same

#Contour Approximation Method

#If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points?
#For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we
#need just two end points of that line. This is what cv2.CHAIN_APPROX_SIMPLE does. It removes all redundant
#points and compresses the contour, thereby saving memory.
#Below image of a rectangle demonstrate this technique. Just draw a circle on all the coordinates in the contour array
#(drawn in blue color). First image shows points I got with cv2.CHAIN_APPROX_NONE (734 points) and second
#image shows the one with cv2.CHAIN_APPROX_SIMPLE (only 4 points). See, how much memory it saves!!!
