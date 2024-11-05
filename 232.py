#recursion
#python also accept function recursion,
#which means a defined function can iteslef.

#example of a recursive function-

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("the factorial of ", num, "is", factorial(num))
