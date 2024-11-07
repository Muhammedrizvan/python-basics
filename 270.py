# Create a class named Vehicle,
# with brand and year properties, and a print_info method:

class vehicle:
    def __init__(self,brand,year):
        self.brnd = brand
        self.year = year

    def print_info(self):
        print(self.brnd,self.year)

car1 = vehicle("innova",2003)
car1.print_info()

#child

class car(vehicle):
    pass

car1 = car("swift",2000)
car1.print_info()
