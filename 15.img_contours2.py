#Moments- most important that the required one should be in white and unwnted in black


#Image moments help you to calculate some features like center of mass of the object, area of the object etc. Check out
#the wikipedia page on Image Moments

import cv2
import numpy as np
img = cv2.imread('img2.jpg',0)
ret,va = cv2.threshold(img,127,255,0)
thresh = cv2.bitwise_not(va)
cv2.imshow("thresh",thresh)
_,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)

#Centroid is given by the relations, Cx =m10/m00
#and Cy = M01/m00
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print cnt
print cx
print cy

#Contour Area M[m00]
area = cv2.contourArea(cnt)
print area


#Contour Perimeter
#It is also called arc length. It can be found out using cv2.arcLength()
#shape is a closed contour (if passed True), or just a curve.
perimeter = cv2.arcLength(cnt,True)
print perimeter

#Contour Approximation
#It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify.
#It is an implementation of Douglas-Peucker algorithm.


epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)


#Below, in second image, green line shows the approximated curve for epsilon = 10% of arc length. Third
#image shows the same for epsilon = 1% of the arc length. Third argument specifies whether curve is
#closed or not.

#Convex Hull

#points,hull(output),clockwise-orientationflag,returnpoints-if true willl return cordinates of hull

hull = cv2.convexHull(cnt)

#But if you want to find convexity defects, you need to pass returnPoints = False.


#Checking Convexity

k = cv2.isContourConvex(cnt)

#Bounding Rectangle
#Straight
x,y,w,h = cv2.boundingRect(cnt)
#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#Rotated Rectangle

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img,[box],0,(0,0,255),2)

#Minimum Enclosing Circle

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
#img = cv2.circle(img,center,radius,(0,255,0),2)

#Fitting an Ellipse


ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(img,ellipse,(0,255,0),2)


#Fitting a Line

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('win',img)
cv2.waitKey(0)






