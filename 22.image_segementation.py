import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('coins.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#Now we need to remove any small white noises in the image. For that we can use morphological opening. To remove
#any small holes in the object, we can use morphological closing.
#So we need to extract the area which we are sure they are coins. Erosion removes the boundary pixels. So whatever
#remaining, we can be sure it is coin. That would work if objects were not touching each other.

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


#See the result. In the thresholded image, we get some regions of coins which we are sure of coins and they are detached now.

#Now we know for sure which are region of coins, which are background and all. So we create marker (it is an array of
#same size as that of original image, but with int32 datatype) and label the regions inside it. The regions we know for
#sure (whether foreground or background) are labelled with any positive integers, but different integers,
#For this we use cv2.connectedComponents(). It labels background of the
#image with 0, then other objects are labelled with integers starting from 1


# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

#It is time for final step, apply watershed. Then marker image will be modified. The boundary region will be marked with -1.


markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]


























