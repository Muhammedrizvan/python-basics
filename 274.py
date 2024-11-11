#add proporties
#add a proporty called "position" to the empolyee

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class employee(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.position = "softwear engineer"



x = employee("muhammed","rizvan")
print(x.position)


