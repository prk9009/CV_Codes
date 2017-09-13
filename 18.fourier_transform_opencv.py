#OpenCV provides the functions cv2.dft() and cv2.idft() for this. It returns the same result as previous, but with two
#channels. First channel will have the real part of the result and second channel will have the imaginary part of the
#result. The input image should be converted to np.float32 first.




import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


#You can also use cv2.cartToPolar() which returns both magnitude and phase in a single shot

#idft lpf applied which blurs the picture

rows, cols = img.shape
crow,ccol = rows/2 , cols/2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
#OpenCV functions cv2.dft() and cv2.idft() are faster than Numpy counterparts. But Numpy functions
#are more user-friendly.


##
##
#laplacian and sobel as filters



import cv2
import numpy as np
from matplotlib import pyplot as plt
# simple averaging filter without scaling parameter
mean_filter = np.ones((3,3))
# creating a guassian filter
x = cv2.getGaussianKernel(5,10)
gaussian = x*x.T
# different edge detecting filters
# scharr in x-direction
scharr = np.array([[-3, 0, 3],
	[-10,0,10],
	[-3, 0, 3]])
# sobel in x direction
sobel_x= np.array([[-1, 0, 1],
		   [-2, 0, 2],
		   [-1, 0, 1]])
# sobel in y direction
sobel_y= np.array([[-1,-2,-1],
		   [0, 0, 0],
		   [1, 2, 1]])
# laplacian
laplacian=np.array([[0, 1, 0],
		    [1,-4, 1],
		    [0, 1, 0]])
filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
filter_name = ['mean_filter', 'gaussian','laplacian', 'sobel_x', \
'sobel_y', 'scharr_x']
fft_filters = [np.fft.fft2(x) for x in filters]
fft_shift = [np.fft.fftshift(y) for y in fft_filters]
mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]
for i in xrange(6):
	plt.subplot(2,3,i+1),plt.imshow(mag_spectrum[i],cmap = 'gray')
	plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
plt.show()





















