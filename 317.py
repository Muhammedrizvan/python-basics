#you can control the numebr of replacments
#by specifying the count parameter!

#replace the first 2 occurance?

import re

txt = "tha arain in spain"
x = re.sub("\s","9",txt,2)
print(x)
