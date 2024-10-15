#update tuples

#chenge tuple values
#once a tuple is creat ,you cannot its values.
#tuples are unchangable ,or immutble as it also is called


#you can convert the tupele into a lsit
#change the list ,and convert the list back into a tuple .

#conveert the tuple into a list to be able to change it

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple (y)
print(x)
