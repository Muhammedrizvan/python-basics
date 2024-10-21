#make a change in the orignal dictionary
#and ee that the values list gets updated as well:

car = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x = car.values()
print(x) #befor the change

car["year"] = 2020
print(x) #after the chnge
