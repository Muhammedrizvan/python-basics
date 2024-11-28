#converting data type on existing array
#the astype() function creates a copy of the array
#and allowss you to specify the data type a a paramter

#change data type from float to integer by using 'i' a parameter value?

import numpy as np

arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
