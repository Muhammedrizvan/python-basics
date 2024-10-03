#the format() method takes unlimited number of argument
#and are placed into the respective placeholders:


quantity = 3
intemno = 567
price = 49.95

myorder = "i want {} pieces of item {} for {} dollers."
print(myorder.format(quantity,intemno,price))
