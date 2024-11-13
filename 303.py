#convert from python to json
#if you have a python object,

#you can convert it into a json string by
#using the json.dumps() method.

#convert from python to json?

import json

x = {
    "name":"john",
    "age":30,
    "city":"new york",
}

y = json.dumps(x)
print(y)
