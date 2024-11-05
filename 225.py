#Default Parameter Value

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def myfunction(counry = "norway"):
    print("i am from " + counry)

myfunction("sweden")
myfunction("london")
myfunction("india")
myfunction()
myfunction("brazil")
