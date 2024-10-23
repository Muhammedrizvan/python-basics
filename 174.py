#loop through nested dictionaries

#you can loop through a dictionary
#by using the items () method like this.

#loop through the keys and values of all nested dictionaries?

myfamily = {
    "child1":{
        "name":"rizvan",
        "year":2003
    },
    "child2": {
        "name":"muhsi",
        "year":2004
    },
    "child3":{
        "name":"illyas",
        "year":2005
    },
}

for x,z in myfamily.items():
    print(x)

    for y in z:
        print(y + ':', z[y])
        