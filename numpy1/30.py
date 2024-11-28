#numpy array copy vs view

#the difference beteween copy and view

#the main deufference between a copy and a view of an array is that:
#the copy is a new array
#and the view i just a view of the original array

#the copy owns the data and
#any changes made to the copy will not affect original array,
#and any changes made to the orginal array will not affect the copy

#the view does not own the date and
#any changes made to the view will affect the original array
#and any changes made to the origanal array will affect the view
