#Canny Edge Detection

#Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in
#horizontal direction (G x ) and vertical direction (G y )

#Edge_Gradient (G) =sqrtt( G^2 x + G^2 y)
#Angle (θ) = tan −1(Gy/Gx)

#Non-maximum Suppression

#full scan of image is done to remove any unwanted pixels which may not constitute the edge
#For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient
#In short, the result you get is a binary image with “thin edges”. 

#Hysteresis Thresholding

#which are all edges are really edges and which are not
#we need two threshold values,minVal and maxVal. Any edges with intensity gradient more than maxVal
# are sure to be edges and those below minVal are sure to be non-edges,
#If they are connected to “sure-edge” pixels, they are considered to be part of edges.

#OpenCV puts all the above in single function, cv2.Canny()


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,100,200) #src , minval, maxval for threshold
#Fourth argument is aperture_size. It is the
#size of Sobel kernel used for find image gradients. By default it is 3. Last argument is L2gradient which specifies the
#equation for finding gradient magnitude. If it is True, it uses the equation mentioned above which is more accurate,
#otherwise it uses this function: Edge_Gradient (G) = |G x | + |G y |. By default, it is False
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
