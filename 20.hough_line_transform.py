#Hough Line Transform
#Itcan detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.
#A line can be represented as y = mx + c or in parametric form, as ρ = x cos θ + y sin θ where ρ is the perpendicular
#distance from origin to the line, and θ is the angle formed by this perpendicular line and horizontal axis measured in counter-clockwise
#Now let’s see how Hough Transform works for lines. Any line can be represented in these two terms, (ρ, θ). So first it
#creates a 2D array or accumulator (to hold values of two parameters)
#Suppose you want the accuracy of angles
#to be 1 degree, you need 180 columns. For ρ, the maximum distance possible is the diagonal length of the image. So
#taking one pixel accuracy, number of rows can be diagonal length of the image


#Consider a 100x100 image with a horizontal line at the middle. Take the first point of the line. You know its (x,y)
#values. Now in the line equation, put the values θ = 0, 1, 2, ...., 180 and check the ρ you get. For every (ρ, θ) pair, you
#increment value by one in our accumulator in its corresponding (ρ, θ) cells. So now in accumulator, the cell (50,90) =
#1 along with some other cells
#Now take the second point on the line. Do the same as above. Increment the the values in the cells corresponding to
#(ρ, θ) you got

#This way, at the end, the cell (50,90) will have maximum votes. So if you search the
#accumulator for maximum votes, you get the value (50,90) which says, there is a line in this image at distance 50 from
#origin and at angle 90 degrees.



##
#It simply returns an array
#of (ρ, θ) values. ρ is measured in pixels and θ is measured in radians. First parameter, Input image should be a
#binary image, so apply threshold or use canny edge detection before finding applying hough transform. Second and
#third parameters are ρ and θ accuracies respectively. Fourth argument is the threshold, which means minimum vote it
#should get for it to be considered as a line.


import cv2
import numpy as np
img = cv2.imread('dave.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('houghlines3.jpg',img)


##
##
#probabilistic Hough transform
#minLineLength - Minimum length of line. Line segments shorter than this are rejected.
#maxLineGap - Maximum allowed gap between line segments to treat them as single line.



import cv2
import numpy as np
img = cv2.imread('dave.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite('houghlines5.jpg',img)




































