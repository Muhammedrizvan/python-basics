#numpy array reshaping
#reshaping arrays
#reshaping means chabging the shape of an array
#the shape of an array is the number of elements in each deamensions.

#reshape from 1-D to 2-D

#convert the following 1-D array with 12 elements into a 2- D

#The outer diamenion will have 4 array each with 3 elemensts:

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)
print(newarr)