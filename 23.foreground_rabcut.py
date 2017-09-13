#How it works from user point of view ? Initially user draws a rectangle around the foreground region (foreground
#region shoule be completely inside the rectangle). Then algorithm segments it iteratively to get the best result.

#arguments

#• img - Input image
#• mask - It is a mask image where we specify which areas are background, foreground or probable back-
#ground/foreground etc. It is done by the following flags, cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD,
#cv2.GC_PR_FGD, or simply pass 0,1,2,3 to image.
#• rect - It is the coordinates of a rectangle which includes the foreground object in the format (x,y,w,h)
#• bdgModel, fgdModel - These are arrays used by the algorithm internally. You just create two np.float64 type
#zero arrays of size (1,65).
#• iterCount - Number of iterations the algorithm should run.
#• mode - It should be cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK or combined which de-
#cides whether we are drawing rectangle or final touchup strokes.


#First let’s see with rectangular mode. We load the image, create a similar mask image. We create fgdModel and
#bgdModel. We give the rectangle parameters. It’s all straight-forward. Let the algorithm run for 5 iterations. Mode
#should be cv2.GC_INIT_WITH_RECT since we are using rectangle. Then run the grabcut. It modifies the mask image.
#In the new mask image, pixels will be marked with four flags denoting background/foreground as specified above.


import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()


#use paint orr some small image manipulation tools to change the picture according to our requirement
#we dont get the correct foreground on our 1st try so we must do some changes


# newmask is the mask image I manually labelled
newmask = cv2.imread('newmask.png',0)
# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1
mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_
˓ → WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()

























































