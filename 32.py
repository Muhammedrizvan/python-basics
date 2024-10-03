#remove whitespace

#whitespace is the space before and/or after th actual text,
#and very often you want to remove this space.

#the strip() method removes any whitespace from the biginning or the end:

a = "              hello, world!                "
print(a.strip())     #returns "hello, world!"
print(a)