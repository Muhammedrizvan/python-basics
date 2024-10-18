# the values true and 1 are consider th esame value
#the same goes for False and 0

#join sets that contains the values
#True,False ,1,and0 ,and see what is consider as duplicate

set1 = {"apple",1,"banana",0,"cherry"}
set2 = {False,"google",1,"apple",2,True}

set3 = set1.intersection(set2)
print(set3)
