#The self Parameter!
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
#It does not have to be named self ,
# you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
# Use the words mysillyobject and abc instead of self?

class person:
    def __init__(mee,name,age):
        mee.name = name
        mee.age = age

    def myfunc(abcd):
        print("my beatiful name is " + abcd.name)

n1 = person("rizvan",21)
n1.myfunc()
