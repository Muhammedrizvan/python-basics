#exit the loop when x is "banana"
#but the time the break comes before the print

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
    