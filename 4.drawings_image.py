#Drawing Functions in OpenCV
import numpy as np
import cv2
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)#start, end, color, size

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)##start diag, end diag, color, size

img = cv2.circle(img,(447,63), 63, (0,0,255), -1)#center, radius, colorr, size, -1 => fill the whole part

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)# center, (major axes length, minor axes length),angle of rotation of ellipse in anti-clockwise direction, startAngle and endAngle, size of line used

#To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where
#ROWS are number of vertices and it should be of type int32. Here we draw a small polygon of with four vertices in
#yellow color.

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

#Adding Text to Images:.

font = cv2.FONT_HERSHEY_SIMPLEX #fint musr be mentioned
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)#source, text , Position, font, sizeof font, color, thickness, lineType
cv2.imshow('ima',img)
cv2.waitKey(0)
cv2.destroyAllWindows
