#you can perform if .. else statment inside the placeholders:
#return "expensive" if the price is over 50 otherwise return "cheep"

price = 49
txt = f"it is very {'expensive' if price>50 else 'cheep'}"
print(txt)
