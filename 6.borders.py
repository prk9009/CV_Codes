#img[100,100] = [255,255,255], it can be changeed
#Image properties include number of rows, columns and channels, type of image data, number of pixels etc.
#print img.shape,print img.size, print img.dtype
#img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is
#caused by invalid datatype.


#Image ROI
#ball = img[280:340, 330:390]
#img[273:333, 100:160] = ball# changing the img with ball at that region


#Splitting and Merging Image Channels
# b,g,r = cv2.split(img) or  b = img[:,:,0]
# img = cv2.merge((b,g,r))

#bordor making check ook for importance
#cv2.copyMakeBorder(param)#src,top, bottom, left, right,borderType
#borderType: 
# – cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next
#argument.
# – cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
# – cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight
#change, like this : gfedcb|abcdefgh|gfedcba
# – cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
# – cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg



##This wont work because of a few \xe2 error just use it to understand




import cv2
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv2.imread('opencv_logo.png')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
