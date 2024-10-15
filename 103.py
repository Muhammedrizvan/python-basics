#append ()method

#convert the tuple into a list ,add "ornage",and
#convert it back into a tuple

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
