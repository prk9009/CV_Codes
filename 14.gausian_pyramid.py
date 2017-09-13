#Image Pyramids

#1) Gaussian Pyramid and 2) Laplacian Pyramids

#Higher level (Low resolution) in a Gaussian Pyramid is formed by removing
# consecutive rows and columns in Lowerlevel (higher resolution) image.
#Then each pixel in higher level is formed by the contribution from 5 pixels in un-
#derlying level with gaussian weights. It is called an Octave
import cv2
import numpy as np

higher_reso = cv2.imread('img.jpg')
lower_reso = cv2.pyrDown(higher_reso)
higher_reso2 = cv2.pyrUp(lower_reso)#higher_reso2 is not equal to higher_reso,
#because once you decrease the resolution, you loose the information
gray1=cv2.cvtColor(higher_reso, cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(higher_reso2, cv2.COLOR_BGR2GRAY)
x=gray1-gray2[:,1:1282]

#L = cv2.subtract(higher_reso,higher_reso2[:,1:1282,:])
#lower = np.array([0,0,245])
#upper = np.array([0,0,255])
#hsv = cv2.cvtColor(x, cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(hsv, lower, upper)
#ret,th1 = cv2.threshold(x,250,255,cv2.THRESH_BINARY)
cv2.imshow('image 1', higher_reso)
cv2.imshow('image 2', lower_reso)
cv2.imshow('image 3', higher_reso2)
cv2.imshow('image 4', x)
cv2.waitKey(0)
cv2.destroyAllWindows()




#blending 2 images

import cv2
import numpy as np,sys
A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
	G = cv2.pyrDown(G)
	gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
	G = cv2.pyrDown(G)
	gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
	GE = cv2.pyrUp(gpA[i])
	L = cv2.subtract(gpA[i-1],GE)
lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
	GE = cv2.pyrUp(gpB[i])
	L = cv2.subtract(gpB[i-1],GE)
	lpB.append(L)
# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
	rows,cols,dpt = la.shape
	ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
	LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
	ls_ = cv2.pyrUp(ls_)
	ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)







