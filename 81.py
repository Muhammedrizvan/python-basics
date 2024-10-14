#perform a case -insentive sort of the list


thislist = ["banana","orange","kiwi","cherry"]
thislist.sort(key=str.lower())
print(thislist)


#the key perameter is set to str.lowe,
#which means that the list will be sorted based
#on the lowercase version of each string element.

#"banana".lower()returns "banana"
#"Orange".lower()returns "orange"
#"kiwi".lower()returns "kiwi"
#"cherry".lower()returns "cherry"
