import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('messi5.jpg',0)#source and type
#cv2.IMREAD_COLOR-	1
#cv2.IMREAD_GRAYSCALE-	0
#cv2.IMREAD_UNCHANGED-	-1
cv2.imshow('image', img)#op and source	 
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.WINDOW_AUTOSIZE
cv2.imwrite('messigray.png',img)#to save it as another file



plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()


#cv2.waitKey(0)#important for checking till when shoukd i wauit
k = cv2.waitKey(0)#simoly means wait -- milliseconds before proceding
#add extra & 0xFF to waitKey(0) if workng on a 64 bit
if k == 27:
# wait for ESC key to exit
#check all keyboard keys values for easier usage of waitKey(0)
cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()	
cv2.destroyAllWindows()#this destroys all stray windows

