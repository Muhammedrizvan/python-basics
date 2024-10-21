#add a new items to the orginal dictionary
#and see that keys list gets updated as well ?

car = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change
