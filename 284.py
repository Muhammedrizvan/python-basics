#class polymorphism

#polymorphism is often used in class method
#where we can have multiple classes with  the same method name.
#diffrent classes with the same method?

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")


class boat:
    def __init__(self, name, type):
        self.brand = name
        self.model = type

    def move(self):
        print("sail")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

car1 = car("toyota","innova")
boat1 = boat("ibza","touring 20")
plane1 = plane("boring","747")

for x in (car1,boat1,plane1):
    x.move()

#we have three classes: car, boat , plane
#and they all have a method called move()
