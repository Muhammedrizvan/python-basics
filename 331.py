#raise a type error if x is not integer?

x = "hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")
