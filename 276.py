# Add a salary parameter,
# and pass the correct salary when creating objects.

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class employee(person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary

x = employee("muhammed","rizvan",10000000)
print(x.salary)

