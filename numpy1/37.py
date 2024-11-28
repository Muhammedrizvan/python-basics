#return copy or view

#check if the return array is a copy or view?

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

#the example above return the original array ,so it is a view
