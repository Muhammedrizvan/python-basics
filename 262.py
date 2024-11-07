# Create a method in the Animal class.
# Insert a function that prints the animal's name and sound,
# and execute it on the a1 object.

class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def animalclass(self):
         print("the animal name is " + self.name )

a1 = animal("cat","meow")
a1.animalclass()
