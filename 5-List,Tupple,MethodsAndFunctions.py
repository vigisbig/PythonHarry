# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#Lists are created using square brackets:

a_list = [90,45,56,23]
another_list = ['Yuvraj','Mayank','Ajit','Pankaj']
yet_another = ['Apple',30,'kg','Banana','Fruits']

# Using len() function, we can find the length of list

print(len(a_list))                  # Length of list
print(a_list[1])                    # To print / select item from a list
print(max(a_list))                  # Returns biggest number in list
print(min(a_list))                  # Returns smallest number in list

"""
List items are ordered, changeable, and allow duplicate values. List items are indexed, the first item has index [0], the second item has index [1] etc.
By ordered we mean, if we add new items to a list, the new items will be placed at the end of the list.
List is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value
"""
# Some of the list methods are show below

a = ['Apple','Banana','Pineapple',"Banana"]

a.append('Grapes')                  # adds an element at the end of list
print(a)            
a.copy()                            # Copies a list
print(a)                      
print(a.count('Banana'))            # Returns the number of elements with the specified value 
b = ['Mahindra','Tata','Bajaj']
a.extend(b)                         # Adds the elements of a list (or any iterable like tuple, list, set etc.), to the end of the current list
print(a)
print(a.index('Banana'))            # Returns the index of the first element with the specified value                   
a.insert(0,'Orange')                # Adds an element at the specified position index
print(a)
a.pop(0)                            # Removes an element at the specified position index
print(a)
a.remove('Banana')                  # Removes the first item with the specified value
print(a)
a.reverse()                         # Reverses the order of the list
print(a)
a.sort()                            # Sorts the list
print(a)
a.clear()                           # Removes all elements form the list
print(a)
a.append(34)                        # Adds an element to the empty list
print(a)
a[0] = 12                           # Changes the element to 12
print(a)                            
#Read more:  https://www.w3schools.com/python/python_ref_list.asp

# Tuple is a collection of objects separated by commas. To create a tuple we will use () operators.
# In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.

tup = (1,)      #   In case your generating a tuple with a single element, make sure to add a comma after the element. 
print(tup)