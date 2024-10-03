
#local variable

def myfunc1():
    z = "fantastic"
    #z is local variable ,can be accessed only inside function.
    print(z)

myfunc1()

#global keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("python is"+ x)
