#This algorithm is an iterative process. We will explain it step-by-step with the help of images.

#Step : 2 - It calculates the distance from each point to both centroids. If a test data is more closer to C1, then that data
#is labelled with ‘0’. If it is closer to C2, then labelled as ‘1’ (If more centroids are there, labelled as ‘2’,‘3’ etc)

#Step : 3 - Next we calculate the average of all blue points and red points separately and that will be our new centroids.
#That is C1 and C2 shift to newly calculated centroids. (Remember, the images shown are not true values and not to
#true scale, it is just for demonstration only).

#Now Step - 2 and Step - 3 are iterated until both centroids are converged to fixed points. (Or it may be stopped
#depending on the criteria we provide, like maximum number of iterations, or a specific accuracy is reached etc.)
#These points are such that sum of distances between test data and their corresponding centroids are minimum.
#Or simply, sum of distances between C1 ↔ Red_P oints and C2 ↔ Blue_P oints is minimum.



#Input parameters
#1. samples : It should be of np.float32 data type, and each feature should be put in a single column


#2. nclusters(K) : Number of clusters required at end
#3. criteria [It is the iteration termination criteria. When this criteria is satisfied, algorithm iteration stops. Actually,
#it should be a tuple of 3 parameters. They are ( type, max_iter, epsilon ):]
#• 3.a - type of termination criteria [It has 3 flags as below:] cv2.TERM_CRITERIA_EPS
#- stop the algorithm iteration if specified accuracy,epsilon,is reached.
#cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of
#iterations, max_iter. cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER -
#stop the iteration when any of the above condition is met.
#• 3.b - max_iter - An integer specifying maximum number of iterations.
#• 3.c - epsilon - Required accuracy
#4. attempts : Flag to specify the number of times the algorithm is executed using different initial labellings. The
#algorithm returns the labels that yield the best compactness. This compactness is returned as output.
#5. flags : This flag is used to specify how initial centers are taken. Normally two flags are used for this :
#cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS.



#Output parameters
#1. compactness : It is the sum of squared distance from each point to their corresponding centers.
#2. labels : This is the label array (same as ‘code’ in previous article) where each element marked ‘0’, ‘1’.....
#3. centers : This is array of centers of clusters.


#Consider, you have a set of data with only one feature, ie one-dimensional.


import numpy as np
import cv2
from matplotlib import pyplot as plt
x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
plt.hist(z,256,[0,256]),plt.show()



#Now we apply the KMeans function. Before that we need to specify the criteria. My criteria is such that, whenever
#10 iterations of algorithm is ran, or an accuracy of epsilon = 1.0 is reached, stop the algorithm and return the
#answer.

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# Set flags (Just to avoid line break in the code)
flags = cv2.KMEANS_RANDOM_CENTERS
# Apply KMeans
compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

#This gives us the compactness, labels and centers.
#Labels will have the samesize as that of test data where each data will be labelled as ‘0’,‘1’,‘2’ etc. depending on 
#their centroids. Now we split the data to different clusters depending on their labels.




# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
plt.hist(A,256,[0,256],color = 'r')
plt.hist(B,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()


#Data with Multiple Features

import numpy as np
import cv2
from matplotlib import pyplot as plt
X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))
# convert to np.float32
Z = np.float32(Z)
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
# Plot the data
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()

#Color Quantization

#Color Quantization is the process of reducing number of colors in an image. One reason to do so is to reduce the
#memory. Sometimes, some devices may have limitation such that it can produce only limited number of colors.


#And after the clustering, we apply centroid values (it is also
#R,G,B) to all pixels, such that resulting image will have specified number of colors. And again we need to reshape it
#back to the shape of original image. Below is the code:


import numpy as np
import cv2
img = cv2.imread('home.jpg')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()














