#1- Create a Person class with firstname and lastname properties.

# Add an _init_ method to initialize these properties.
# Add a printname method to print the full name.

#2- Create a Student class that inherits from the Person class.
# Add a property called graduationyear to the Student class,
# with a default value of 2025.
# Modify the Student class so that you can pass
# a specific graduation year when creating an object.

#3- Write code to:

# Create an object of the Student class,
# using the name "Anna Smith" and a graduation year of 2023.
# Print the first name second name and graduation year.

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,graduationyear):
        super().__init__(fname,lname)
        self.graduationyear = graduationyear
    def print_details(self):
        print(f"{self.firstname}{self.lastname}"
              f"graduation year:{self.graduationyear}")
student = student("muhammed","rizvan",2020)
student.print_details()


