#upper using list comprehension

#set the vlue in the new list to upper case ?

fruits =  ["apple","banana","cherry","kiwi","mango"]
fruits1 = ["APPLE","BANANA","CHERRY","KIWI","MANGO"]
newlist = [x.upper() for x in fruits]
newlist1 = [x.lower() for x in fruits1]
print(newlist)
print(newlist1)

