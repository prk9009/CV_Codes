#Smoothing Images


#As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF),
#etc. A LPF helps in removing noise, or blurring the image. A HPF filters helps in finding edges in an image.
#OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image. As an example, we will try an
#averaging filter on an image. A 5x5 averaging filter kernel can be defined as follows


#2D Convolution ( Image Filtering )


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)## LPF, check that -1
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


#Averaging

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.png')
blur = cv2.blur(img,(5,5))# 2d conv function not required, it is useful fr hpf or any other type of matix convolution
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


#Gaussian Filtering

blur = cv2.GaussianBlur(img,(5,5),0)# same as above code just changing the name and an extra argument of sd in x direction and sd in y direction


#Median Filtering3


median = cv2.medianBlur(img,5)


# Bilateral Filtering highly effective at noise removal while preserving edges

blur = cv2.bilateralFilter(img,9,75,75)  ## check all the parameters online once


