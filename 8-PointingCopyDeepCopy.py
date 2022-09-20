import copy

print("  ")
print("########### How things work in a nested list ################")
print("\n")
a = [['a',2,3],[4,5,6]]           
b = a
print("a = ",a)
print("b = ", b)
print("---------------- Result of b = a ------------")
print("  ")
print("Changing a[0][0] = 1")
a[0][0] = 1
print("a =",a,"\nb =",b) 
print("Adding [7,8,9]")
a.append([7,8,9])
print("a =",a,"\nb =",b) 


a = [['a',2,3],[4,5,6]]           

b = a.copy()

print("  ")
print("------------ Result of b = a.copy() ----------")
print("  ")
print("Changing a[0][0] = 1")

a[0][0] = 1
print("a =",a,"\nb =",b)
print("Adding [7,8,9]")
a.append([7,8,9])
print("a =",a,"\nb =",b) 

a = [['a',2,3],[4,5,6]]           

b = copy.deepcopy(a)

print("  ")
print("---------- Result of b = copy.deepcopy(a) ----------")
print("  ")
print("Changing a[0][0] = 1")
a[0][0] = 1
print("a =",a,"\nb =",b)
print("Adding [7,8,9]")
a.append([7,8,9])
print("a =",a,"\nb =",b) 

print("  ")

print("########### How things work in a normal list ################")
print("  ")

l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
l4 = copy.deepcopy(l1)

print(l1,l2,l3,l4)

del l1[0]
print(l1,l2,l3,l4)