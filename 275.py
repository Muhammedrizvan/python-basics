#add a year parameter,
#and pass the correct year when creat objects

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year


x = student("muhammed","rizvan",2019)
print(x.graduationyear)
