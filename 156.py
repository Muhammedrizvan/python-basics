#add a new items to the original dictionary
#and see that items gets updated as well

car = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x)  #after the change

