#fainally
#the finally block if specified
#will be exicuted regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("somthing went wrong")
finally:
    print("the 'try except'is finished")
    