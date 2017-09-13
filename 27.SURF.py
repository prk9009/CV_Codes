#Analysis shows it is 3 times faster than SIFTwhile performance is comparable to SIFT. SURF is good at handling images
# with blurring and rotation, but not good at handling viewpoint change and illumination change

#OpenCV provides SURF functionalities just like SIFT. You initiate a SURF object with some optional conditions like
#64/128-dim descriptors, Upright/Normal SURF etc.

#terminal implementation

>>> img = cv2.imread('fly.png',0)
# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
>>> surf = cv2.SURF(400)
# Find keypoints and descriptors directly
>>> kp, des = surf.detectAndCompute(img,None)
>>> len(kp)
699
#1199 keypoints is too much to show in a picture. We reduce it to some 50 to draw it on an image. While matching, we
#may need all those features, but not now. So we increase the Hessian Threshold.

# Check present Hessian threshold
>>> print surf.hessianThreshold
400.0
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
>>> surf.hessianThreshold = 50000
# Again compute keypoints and check its number.
>>> kp, des = surf.detectAndCompute(img,None)
>>> print len(kp)
47
>>> img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
>>> plt.imshow(img2),plt.show()

#Now I want to apply U-SURF, so that it won’t find the orientation.

# Check upright flag, if it False, set it to True
>>> print surf.upright
False
>>> surf.upright = True
# Recompute the feature points and draw it
>>> kp = surf.detect(img,None)
>>> img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
>>> plt.imshow(img2),plt.show()

#Finally we check the descriptor size and change it to 128 if it is only 64-dim.

# Find size of descriptor
>>> print surf.descriptorSize()
64
# That means flag, "extended" is False.
>>> surf.extended
False
# So we make it to True to get 128-dim descriptors.
>>> surf.extended = True
>>> kp, des = surf.detectAndCompute(img,None)
>>> print surf.descriptorSize()
128
>>> print des.shape
(47, 128)
































