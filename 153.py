#add a new items to the original dictionary
#and see that the value list gets update as well:

car = {
    "brand":"ford",
    "model":"mustang",
    "yaer":1964
}
x = car.values()
print(x) #befor the chsnge

car["color"] = "red"
print(x)  #after the change
