#3-D arrays
#an  array  that  has 2-d arrays (matrices) as its elements is called 3-D array.
#these are often used to reperent a 3rd order tensor.

#creat a 3-D array with two 2-D arrays
#both containing two arrays with value 1,2,3 and 4,5,6?

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)
