#Image Gradients Find Image gradients, edges

#Sobel and Scharr Derivatives
#Sobel operators is a joint Gausssian smoothing plus differentiation operation,so it is more resistant to nois
#Youcan specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder
#respectively)
#If ksize = -1, a 3x3 Scharr filter is used
#which gives better results than 3x3 Sobel filter

#LapLacian
#It calculates the Laplacian of the image given by the relation
#∆src = ∂ ∂x src
#+ ∂ ∂y sr
#ksize = 1


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('dave.jpg',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)##check params
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)##chec params
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

#IMP
#In our last example, output datatype is cv2.CV_8U or np.uint8
#Black-to-White transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken as a Negative slope
#(It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. In simple words, you
#miss that edge
#If you want to detect both edges, better option is to keep the output datatype to some higher forms, like cv2.CV_16S,
#cv2.CV_64F etc, take its absolute value and then convert back to cv2.CV_8U

#check and understand
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('box.png',0)
# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()
