#remove itms
#note: you cannot remove items in a tuple

#tuples are unchangable,so you cannot remove items form it
#but you can use the same workround as we used for changing
#and adding tuple items

#convert the tuple into a list , remove "apple"
#and convert it back into a tuple

thistuple = ("apple","banana","chery")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
