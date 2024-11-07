#modify object proporties
#you can modify proporties on objects likes this


#set the age of p1 to 40?
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hii my name is " + self.name)

p1 = person("rizvan",25)

p1.age = 21
print(p1.age)
