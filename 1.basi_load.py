import cv2
image = cv2.imread('img3.jpg')#('img3.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
			      #	CV_LOAD_IMAGE_COLOR,CV_LOAD_IMAGE_UNCHANGED
cv2.imwrite('img.jpg', image)
cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#An OpenCV image is a 2D or 3D array of type numpy.array
