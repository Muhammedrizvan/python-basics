#access 2-D arrays
#to access elements from 2-D array we can use
#comma seperated integers representing the dimensions
#and the index of the element


#think of 2-D arrays like a table with rows and columns,
#where the diemnesions representing th row and the index represent the column

#access the element on the first row second column

import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row:',arr[0,1])#row index numer,element index number
print('5th element on 2nd row',arr[1,4])

