#you can use that &operator
#instead of the intersection() method
#and you will get that same result.

#use & to join two sets

set1 = {"apple","banana","cherry"}
set2 = {"google","microsft","apple"}

set3 = set1&set2
print(set3)

#the & operator only allows you to join sets with sets
#and not with other date types
#like you can with the interaection() method
