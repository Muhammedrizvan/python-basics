#copy
#make a copy change the original array,and display both array?

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#the copy should not be affected by the changes made to the original array
