#using a while loop
#you can loop through the tuple items by using a while loop


#use the len() function to determine the length of the tuple
#then strts at 0 and loop your way through the tuple items by
#referring to their indexes .

#remeber to increas the index by 1 after each iteratin
#print all items ,using a while loop to go through all the index numbers

thistuple = ("apple","banana","cherry",)
i=0
while i <len(thistuple):
    print(thistuple[i])
    i = i+1
    