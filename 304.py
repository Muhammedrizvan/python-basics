#convert a python object containg all the leagul data types

import json
x = {
    "name":"john",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("ann","billy"),
    "pets":None,
    "cars":[
        {"model":"bmw 230","mpg":27.5},
        {"model":"ford edge","mpg":24.1}
    ]
}
print(json.dumps(x))
