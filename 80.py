#customize sort function

#you can also customize your own function by
#using the keyword argument key = function
#the function will return
#a number that will be used to sort the list (the lowest number first )

#sort the list based on how close the numebr is to 50?

def myfunc(n):
    return abs(n-50)

thislist = [100,50,65,82,23]

thislist.sort(key=myfunc)
print(thislist)


#myfunc(100) returns abs (100-50) = 50
#myfunc(50) returns abs (50-50)= 0
#myfunc(65) returns abs (65-50)= 15
#myfunc(82) returns abs (82-50)= 32
#myfunc(23) returns abs (23-50)= 27

#the list is sorted based on these returns values :
#50(from 100)
#0(from 65)
#15(from 82)
#27(from 23)
#the sorted order of the list will be: [50,65,23,82,100]
#which corresponds to sorting by the absolute diffrence from 50.
