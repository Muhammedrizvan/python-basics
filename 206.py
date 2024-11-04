#the condinue statment
#with the continue statment we can stop
#the current itertion of the loop ,
#and continue with the next:

#do not print banana?

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
