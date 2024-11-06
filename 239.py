#lambda functions

#function definition to make a function
#that always double the number you send in?


#function definition:
def myfunc(n):
    return lambda a : a * n


#myfunc takes one argumwnt n.
#it return a lambda function lambda a : a * n,
#which is an anonymous (unnamed) function.
#this lambda takes one argument a and returns the result of a * n.


#creat a multiplier:
mydoubler = myfunc(2)


#here, myfunc(2) is called with n = 2
#this returns a lambada function equivalent to
#lambda a : a * 2 (becaus n is 2)
#mydoubler now hols a reference to this lambda function,
#so mydoubler(a) will double any input a.

print(mydoubler(11))
