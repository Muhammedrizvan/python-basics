#print the position (start- and end-poation) of
#the first match occursnce
#the regular expression looks for any words
#that starts with an upper case "s"?

import re
txt = "the rain in spain"
x = re.search(r"\bs\w+",txt)
print(x.span())
