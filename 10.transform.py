#Geometric Transformations of Images
#cv2.getPerspectiveTransform
#cv2.warpAffine
#cv2.warpPerspective
#cv2.INTER_AREA
#cv2.INTER_CUBIC
#cv2.INTER_LINEAR
#Translation

import cv2
import numpy as np
img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]]) # for translation we need a M of 	[1 0 tx]
#	[0 1 ty]
dst = cv2.warpAffine(img,M,(cols,rows))# source, wrapAffine matrix M, cols and rows of the output image
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Rotation

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)# check the param
dst = cv2.warpAffine(img,M,(cols,rows))

#Affine


img = cv2.imread('drawing.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)# for affine we ned 3 pts in common so M creates an M with the points as nescessary
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


#perspective



img = cv2.imread('sudokusmall.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)# for perspective transform we need 4 points
dst = cv2.warpPerspective(img,M,(300,300))# src, matrix , rows and cols of output img
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

