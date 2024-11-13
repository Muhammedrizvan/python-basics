#Format the Result
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

#Use the indent parameter to define the numbers of indents?
print(json.dumps(x,indent=4))
