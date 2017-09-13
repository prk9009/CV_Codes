#We will do a simple example here, with two families (classes), just like above. Then in the next chapter, we will do
#much more better example.
#So here, we label the Red family as Class-0 (so denoted by 0) and Blue family as Class-1 (denoted by 1). We create
#25 families or 25 training data, and label them either Class-0 or Class-1. We do all these with the help of Random
#Number Generator in Numpy.
#Then we plot it with the help of Matplotlib. Red families are shown as Red Triangles and Blue families are shown as
#Blue Squares.


import cv2
import numpy as np
import matplotlib.pyplot as plt
# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)
# Take Red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')
plt.show()
#Next initiate the kNN algorithm and pass the trainData and responses to train the kNN (It constructs a search tree).

#Our data should be a floating point array
#specify how many neighbours we want. It returns:
#1. The label given to new-comer depending upon the kNN theory we saw earlier. If you want Nearest Neighbour
#algorithm, just specify k=1 where k is the number of neighbours.
#2. The labels of k-Nearest Neighbours.
#3. Corresponding distances from new-comer to each nearest neighbour.

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
knn = cv2.ml.KNearest()
knn.train(trainData,responses)
ret, results, neighbours ,dist = knn.find_nearest(newcomer, 3)
print "result: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist
plt.show()

# 10 new comers
newcomers = np.random.randint(0,100,(10,2)).astype(np.float32)
ret, results,neighbours,dist = knn.find_nearest(newcomer, 3)
# The results also will contain 10 labels.






