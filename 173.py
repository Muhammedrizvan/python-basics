#access items in nested dictionaries

#print the name of child 2?
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
print(myfamily["child2"]["name"])
