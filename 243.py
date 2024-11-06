# function definition to make both function (double,triple)
#in the same programm?

def myfunction(n):
    return lambda a : a * n
mydoubler = myfunction(2)
mytripler = myfunction(3)

print(mydoubler(5))
print(mytripler(3))
