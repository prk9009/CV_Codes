#• img - Input image, it should be grayscale and float32 type.
#• blockSize - It is the size of neighbourhood considered for corner detection
#• ksize - Aperture parameter of Sobel derivative used.
#• k - Harris detector free parameter in the equation.


import cv2
import numpy as np
filename = 'chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
cv2.destroyAllWindows()


#cv2.cornerSubPix() which further refines the corners detected with sub-pixel accuracy.
#we need to find the harris corners first. Then we pass the centroids of these corners (There may be a bunch of
#pixels at a corner, we take their centroid) to refine them. Harris corners are marked in red pixels and refined corners
#are marked in green pixels. For this function, we have to define the criteria when to stop the iteration. We stop it after
#a specified number of iteration or a certain accuracy is achieved,


import cv2
import numpy as np
filename = 'chessboard2.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv2.imwrite('subpixel5.png',img)














































