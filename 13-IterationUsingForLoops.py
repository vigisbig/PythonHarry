# For loop runs till the time it runs out of elements in the list,set,tuple etc.
# One way of iterating list

l1 = ["Ajit", "Vanshika", "Radhu", "Jagmohan"]

for names in l1:
    print(names)

#Another way to do it if the list is nested and is in following format

l2 = [["Ajit", "Maggi"], ["Vanshika","Rajma"], ["Radhu","Chole"], ["Jagmohan","Lassan"]]

for names,food in l2:
    print(names, "likes", food)

# Creating dictionary from list, see how syntax changes and see how we iterate dictionaries

d1 = dict(l2)
print(d1)               
for names,food in d1.items():                 #     Syntax for key:value pairs      
    print(names, "likes", food)
for names in d1:                              #     Syntax for key only
    print(names)
