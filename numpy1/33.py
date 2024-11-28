#check if array owns it data

#copied owns the data
#and view does not own the data ,
#but how can we check this?-----using base
#base that return none if the array owns the data .
#otherwise the  base attribute rfefrs to the original object

#print the value of the base attribute to
#check if an array owns it's data or not?

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
#the copy return none.
#the view returns the original arry
