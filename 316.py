#the sub() function
#the sub() function replace the matches with the text of your choice

#repalce every white-space charecter with the number

import re

txt = "the rain in spain"
x = re.sub("\s","9",txt)
print(x)
