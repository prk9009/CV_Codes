#Histograms - 3 : 2D Histograms

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('img.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 2], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist,interpolation = 'nearest')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



#refer more 121 for further imrtance

#Histogram - 4 : Histogram Backprojection
#the output image will
#have our object of interest in more white compared to remaining part.

#We create a histogram of an image containing our object of interest (in our case, the ground
#The object should fill the image as far as possible for better results. And a color histogram
#is preferred over grayscale histogram, because color of the object is more better way to define the object than its
#grayscale intensity. We then “back-project” this histogram over our test image where we need to find the object, ie in
#other words, we calculate the probability of every pixel belonging to the ground and show it. The resulting output on
#proper thresholding gives us the ground alone.

#Algorithm in Numpy

import cv2
import numpy as np
from matplotlib import pyplot as plt
#roi is the object or region of object we need to find
roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#target is the image we search in
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )


#Find the ratio R = M
#I . Then backproject R, ie use R as palette and create a new image with every pixel as its
#corresponding probability of being target. ie B(x,y) = R[h(x,y),s(x,y)] where h is hue and s is saturation
#of the pixel at (x,y). After that apply the condition B(x, y) = min[B(x, y), 1].

h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

#Now apply a convolution with a circular disc, B = D * B, where D is the disc kernel.

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

#Now the location of maximum intensity gives us the location of object. If we are expecting a region in the image,
#thresholding for a suitable value gives a nice result.

ret,thresh = cv2.threshold(B,50,255,0)

#thats it



#direct


import cv2
import numpy as np
roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)
# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
res = np.vstack((target,thresh,res))
cv2.imwrite('res.jpg',res)

