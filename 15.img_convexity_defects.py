#Convexity Defects
#bas16.py
#hull = cv2.convexHull(cnt,returnPoints = False)
#defects = cv2.convexityDefects(cnt,hull)


#It returns an array where each row contains these values - [ start point, end point, farthest point, approximate
#distance to farthest point ]. We can visualize it using an image. We draw a line joining start point and end point, then
#draw a circle at the farthest point. Remember first three values returned are indices of cnt. So we have to bring those
#values from cnt.


import cv2
import numpy as np
img = cv2.imread('img.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
contours = cv2.findContours(thresh,2,1)
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	cv2.line(img,start,end,[0,255,0],2)
	cv2.circle(img,far,5,[0,0,255],-1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Point Polygon Test
#This function finds the shortest distance between a point in the image and a contour.

dist = cv2.pointPolygonTest(cnt,(50,50),True)
#In the function, third argument is measureDist. If it is True, it finds the signed distance. If False, it finds
#whether the point is inside or outside or on the contour (it returns +1, -1, 0 respectively).


#Match Shapes
#cv2.matchShapes() which enables us to compare two shapes, or two contours and
#returns a metric showing the similarity.calculated based on thehu-moment values. Different measurement methods are explained in the doc

import cv2
import numpy as np
img1 = cv2.imread('star.jpg',0)
img2 = cv2.imread('star2.jpg',0)
ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret

#Hu-Moments are seven moments invariant to translation, rotation and scale. Seventh one is skew-invariant. Those
#values can be found using cv2.HuMoments() function.



#Check the documentation for cv2.pointPolygonTest(), you can find a nice image in Red and Blue color.

#Compare images of digits or letters using cv2.matchShapes(). ( That would be a simple step towards OCR )







