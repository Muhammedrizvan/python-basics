#shape of an array
#the shape of an array is the numnber of elements in each diamenion.

#numpy arrays have an attrubute called shape that returns
#a tuple with each index having the number of corresponding elements.

#print the shape of a 2-D array?

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr.shape)
#1,2,3,4
#4,5,6,7  = 2 row and 4 columns
# #the example above returns (2,4) which means that
#the array hase 2 diamensions
#where the first diamenipns has 2 elements and the second has 4
