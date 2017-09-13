#Morphological Transformations

#Erosion
#it erodes away the boundaries of foreground object
#The kernel slides through the image (as in 2D convolution)
#all the pixels near boundary will be discarded depending upon the size of kernel.
#a 5x5 kernel with full of one

import cv2
import numpy as np
img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

#Dilation

#in cases like noise removal, erosion is followed by dilation
#Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since
#noise is gone, they won’t come back, but our object area increases. It is also useful in joining broken parts of an object.
dilation = cv2.dilate(img,kernel,iterations = 1)

#Opening

#Opening is just another name of erosion followed by dilation.
#


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) ## check the params

# Closing

#Closing is reverse of Opening, Dilation followed by Erosion

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)### check the params

#Morphological Gradient

#It is the difference between dilation and erosion of an image.

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


#Top Hat
#It is the difference between input image and Opening of the image..

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


#Black Hat

#It is the difference between the closing of the input image and input image.

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# to make an automatic kernal instead of doing it manally
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0]], dtype=uint8)





