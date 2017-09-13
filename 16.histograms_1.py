#Histograms - 1 : Find, Plot, Analyze !!!

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])# channels are [0,1,2,3] depending on the color u mant, 
#mask= None if no region of interest else a mask of b/w image is supplied, histSize= no. of bins, ranges=[0,256] ie all the values u want

#hist in numpy is lot easier than opencv cv2.line

#hist,bins = np.histogram(img.ravel(),256,[0,256])#in numpy

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('home.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
histr = cv2.calcHist([img],[i],None,[256],[0,256])
plt.plot(histr,color = col)
plt.xlim([0,256])
plt.show()


#using opencv pg112

#application of mask

img = cv2.imread('home.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221),
plt.subplot(222),
plt.subplot(223),
plt.subplot(224),
plt.xlim([0,256])
plt.imshow(img, 'gray')
plt.imshow(mask,'gray')
plt.imshow(masked_img, 'gray')
plt.plot(hist_full), plt.plot(hist_mask)
plt.show()


#Histograms - 2: Histogram Equalization


#Consider an image whose pixel values are confined to some specific range of values only. For eg, brighter image will
#have all pixels confined to high values. But a good image will have pixels from all regions of the image.

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('wiki.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]

#Histogram Equalization

img = cv2.imread('wiki.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)

#). Its input is just grayscale image and output is our histogram equalized image.

#So now you can take different images with different light conditions, equalize it and check the results.


#CLAHE (Contrast Limited Adaptive Histogram Equalization)

#It is true that the background contrast has improved after histogram equalization. But compare the face of statue in
#both images. We lost most of the information there due to over-brightness. It is because its histogram is not confined
#to a particular region as we saw in previous cases
#So to solve this problem, adaptive histogram equalization is used. In this, image is divided into small blocks called
#“tiles” (tileSize is 8x8 by default in OpenCV). Then each of these blocks are histogram equalized as usual
#If noise is there, it will be amplified.
#To avoid this, contrast limiting is applied


import numpy as np
import cv2
img = cv2.imread('tsukuba_l.png',0)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)




