"""In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by comma. Dictionary holds pairs of values, 
one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any data type and can be duplicated, 
whereas keys cannot be repeated and must be immutable. """

n1 = {1:1, 2:2, 3:3, 4:4, 5:5}                                  # Created dictionary n1
n2 = {1:"Arjun",2:"Barun",3:"Ganesh",4:"Tarun",5:"Harry"}       # Created dictionary n2

print(n1,n2)                                                    # Printing dictionaries n1, n2

n3 = {'Names': n2, 'Numbers': n1}                               # Created n3 by combining n1 and n2

print(n3)                                                       # Printing dictionary n3

print(n3['Names'][1])                                           # Querying n3['Names'][1]

n3['l1'] = ["Hello", "World"]                                   # Adding a list L1 to n3 dictionary
n3['T1'] = "Hello", "Jee"                                       # Adding a Tupple T1 to n3 dictionary
n3['Library'] = "Books"                                         # Adding a new key:value pair

print(type(n3['l1']))                                           # Checking type of data element
print(type(n3['T1']))                                           # Checking type of data element
print(type(n3['Library']))                                      # Checking type of data element

print(n3)                                                       # Printing n3

del n3['Names'][1]                                              # Using del keyword to delete an element from dictionary, can be used for list,variable,tuple etc. 
print(n3)                                                       # Printing n3


# Understanding  Reference, Shallow copy, and Deep copy in context of dictionary
# Reference make both point to the same data, modifying original will modify both
# Shallow copy makes two seperate copies but they have the same reference data, so modifying will modify other too
# to the extent that it modifies exiting elements of the list

# To understand difference between shallow and deep copy read file 8-PointingCopyDeepCopy