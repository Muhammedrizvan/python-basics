#Object Methods
#Objects can also contain methods.
# Methods in objects are functions that belong to the object.

#create a method in the Person class?

#Insert a function that prints a greeting, and execute it on the p1 object?

class person:
    def __init__(self,name,age): #name and age is proporty
        self.name = name
        self.age = age


    def myfunc(self): #myfunc is the method
        print("hi my name is " + self.name)

p1 = person("rizvan",21) #p1 is object
p1.myfunc()
