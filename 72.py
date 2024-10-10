#without list coprehension
#you will have to write a for satment with a conditional test inside:

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []


for x in fruits:
    if"a"in x:
        newlist.append(x)

print(newlist)



#using list cpmprehension

fruits1 =  ["apple","banana","cherry","kiwi","mango"]

newlist1 = [x for x in fruits1 if "a"in x]

print(newlist1)

