# Write a Python function, power_func,
# that takes one argument n and returns a lambda function
# that raises any number passed to it to the power of n.
# In the same program, create both square and cube functions using power_func.
# Test them by squaring the number 5 and cubing the number 3.

def power_func(n):
    return lambda a : a ** n

sqr = power_func(2)
trpl = power_func(3)

print(sqr(10))
print(trpl(4))

