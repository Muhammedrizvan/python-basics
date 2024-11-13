#match object

#a match object is an object containgin
#information about the search and the result.
#if there is no match
#the value none will return a match object?

import re
txt = ("the rain in spain ")
x = re.search("ai",txt)
print(x)   # this will print an ibject
