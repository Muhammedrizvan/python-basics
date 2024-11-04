#nested if

#if statment inside if statment
#this is called nested if statment.

x = 41

if x > 10:
    print("10")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20.")
else:
    print("below 10")
