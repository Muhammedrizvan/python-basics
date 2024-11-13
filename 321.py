#print the parst of the string wherre there was a match
#the regular expression

#look fro any words that starts with an upper case
import re
txt = "the rain in spain"
x = re.search(r"\bs\w+",txt)
print(x.group())
