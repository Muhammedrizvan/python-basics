#many exception

#you can define as many exception blocked as you want ,
#e.g if you want to execute a specil block of code
#for a special kind of error

#print ine message if the try block raises a name eroor
#and another for other errors?

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("somthing else went wrong")
    