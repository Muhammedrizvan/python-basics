#you can use index numbers {0}
#to be sure the argument are placed in the correct placeholders:


quantity = 3
itemno = 567
price = 49.95
myorder = "i want to pay {2} dollers for {0} pieces of item {1}"

print(myorder.format(quantity,itemno,price))
