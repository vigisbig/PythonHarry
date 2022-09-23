"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members. Define using []
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Defined using ()
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. Defined using {}
Dictionary is a collection which is ordered** and changeable. No duplicate members. Defined using {}

"""

s = set()                                   # created an empty set s
print(type(s))                              # Finding the class type of s
print(s)

s.add(1)                                    # Added one element in set
print(s)

l1 = [1,2,3,3,5,6,5,67,7,4,4,89,9,9,9,9]    # Creating a list l1
set_from_list = set(l1)                     # Creating a set from list l1
print(type(set_from_list))                  # printing class type of set_from_list

print(set_from_list)                        # Printing the set showing that it does not allow duplicate values.



# Read more: https://www.geeksforgeeks.org/python-set-methods/
# Read more: https://www.geeksforgeeks.org/sets-in-python/