#The _str_() Function

#The _str_() function controls what should be returned
# when the class object is represented as a string.

#If the _str_() function is not set,
# the string representation of the object is returned:

#The string representation of an object WITHOUT the _str_() function?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = person("rizvan",21)
print(p1)



class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("rizvan",21)
print(p1)