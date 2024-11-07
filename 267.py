#delete object
#you can delete objects by using the del keyword:

#delete the p1 object?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my friend name is " + self.name)

p1 =person("illyas",22)

del p1
print(p1)
