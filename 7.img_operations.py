#adding images with weights
#img1 = cv2.imread('ml.png')
#img2 = cv2.imread('opencv_logo.jpg')
#dst = cv2.addWeighted(img1,0.7,img2,0.3,0), the extrea zero is any extra addition of value acording to dst= α · img1 + β · img2 + γ
#cv2.imshow('dst',dst)


#Bitwise Operations
#
# Load two images
e1 = cv2.getTickCount()#start time
img1 = cv2.imread('messi5.jpg')#image 1
img2 = cv2.imread('opencv_logo.png')#image 2
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)# will come in a later bas
mask_inv = cv2.bitwise_not(mask)# operation
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)#
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
e2 = cv2.getTickCount()#end time for time of execution
time = (e2 - e1)/ cv2.getTickFrequency() #total time for execution
#for performance optimaization check pg 44 of the book

