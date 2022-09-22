# One way of iterating list

l1 = ["Ajit", "Vanshika", "Radhu", "Jagmohan"]

for names in l1:
    print(names)

# Another way to do it if the list is nested

l2 = [["Ajit", "Maggi"], ["Vanshika","Rajma"], ["Radhu","Chole"], ["Jagmohan","Lassan"]]

for names,food in l2:
    print(names, "likes", food)
