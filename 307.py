#Order the Result

# The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter
# to specify if the result should be sorted or not:

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

print(json.dumps(x,indent=4,sort_keys=True))
