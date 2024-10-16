#using astrisk*

#if the number of variable is less than the number of value,
#you can add an * to the variable name
#and the values will be asssined to the variable as a list

#assign the rest of the values as a list called "red"

fruits = ("apple","banana","cherry","strawberry","raspberry")

(green,yellow,*red) = fruits

print(green)
print(yellow)
print(red)
