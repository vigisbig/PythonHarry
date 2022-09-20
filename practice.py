l1 = [1,2,3]
l2 = l1.copy()

print(l1,l2)

del l1[0]
print(l1,l2)

l3 = [[1,2,3],[4,5,6]]
l4 = l3.copy()
print(l3,l4)
del l3[0][0]
print(l3,l4)