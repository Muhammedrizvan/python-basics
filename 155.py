#make changes in the original dictionary
#and see that the items list gets updated as wekk:

car = {
    "barnd":"ford",
    "model":"mustang",
    "yaer":1964
}
x = car.items()
print(x)  #befor the change

car["yaer"] = 2020
print(x) #after the change
