#delete object proporties

#you can delete proporties on objects by using the del keyword
#delete the age proporty from the p1 objct ?

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)


p1 = person("rizvan",21)

del p1.age
print(p1.age)
