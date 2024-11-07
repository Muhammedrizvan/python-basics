
# Create a method in the Book class.
# Insert a function that returns a formatted string
# with the book title and author,
# and execute it on the b1 object.

class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def bookclass(self):
        print("the book name is " + self.name)

b1 = book("mathilukal","vaikam muhammed basheer")
b1.bookclass()
