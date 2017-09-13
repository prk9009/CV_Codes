#Our problem is, we want to draw our 3D coordinate axis (X, Y, Z axes) on our chessboard’s first corner. X axis in
#blue color, Y axis in green color and Z axis in red color.

import cv2
import numpy as np
import glob
# Load previously saved data
with np.load('B.npz') as X:
mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

#Now let’s create a function, draw which takes the corners in the chessboard (obtained using
#cv2.findChessboardCorners()) and axis points to draw a 3D axis

def draw(img, corners, imgpts):
	corner = tuple(corners[0].ravel())
	img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
	img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
	img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
	return img


#we create termination criteria, object points (3D points of corners in chessboard) and axis
#points. Axis points are points in 3D space for drawing the axis. We draw axis of length 3 (units will be in terms of
#chess square size since we calibrated based on that size). So our X axis is drawn from (0,0,0) to (3,0,0), so for Y axis.
#For Z axis, it is drawn from (0,0,0) to (0,0,-3). Negative denotes it is drawn towards the camera.



criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)


#Search for 7x6 grid. If found, we refine it with subcorner pixels. Then to calculate
#the rotation and translation, we use the function, cv2.solvePnPRansac(). Once we those transformation matrices,
#we use them to project our axis points to the image plane. In simple words, we find the points on image plane
#corresponding to each of (3,0,0),(0,3,0),(0,0,3) in 3D space. Once we get them, we draw lines from the first corner to
#each of these points using our draw() function



for fname in glob.glob('left*.jpg'):
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
	if ret == True:
		corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
		# Find the rotation and translation vectors.
		rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, 			corners2, mtx, dist)
		# project 3D points to image plane
		imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
		img = draw(img,corners2,imgpts)
		cv2.imshow('img',img)
		k = cv2.waitKey(0) & 0xff
		if k == 's':
			cv2.imwrite(fname[:6]+'.png', img)
cv2.destroyAllWindows()


#Render a Cube
#If you want to draw a cube, modify the draw() function and axis points as follows.

def draw(img, corners, imgpts):
	imgpts = np.int32(imgpts).reshape(-1,2)
	# draw ground floor in green
	img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
	# draw pillars in blue color
	for i,j in zip(range(4),range(4,8)):
		img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
		# draw top layer in red color
	img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

	return img
axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])





















