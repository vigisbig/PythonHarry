"""String Slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end.""" 

# Slicing can be done in two ways:

# Using a slice() method
# Using List/Array slicing  [ : : ] method

# Using slice() method

a = "Pankaj"
print(len(a))               # Can be used to find length of string
print(a.index("k"))         # Prints index of first occurence of letter k
print(a.index("a",2,5))     # Prints index of letter 'a' between index 2, 5 

"""The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step)."""

# Syntax:

# slice(stop)
# slice(start, stop, step)

"""
 start: Starting index where the slicing of object starts. stop: Ending index where the slicing of object stops. 
 step: It is an optional argument that determines the increment between each index for slicing. 
 Return Type: Returns a sliced object containing elements in the given range only. 

"""
a = "STRINGYTHINGHY"
s1 = slice(3)
s2 = slice(1, 6, 2)
s3 = slice(-1, -12, -2)
 
print(a[s1])
print(a[s2])
print(a[s3])

print("--------------------------")

# Using array slicing

# [start:stop]          # items start through stop-1
# [start:]              # items start through the rest of the array
# [:stop]               # items from the beginning through stop-1
# [:]                   # a copy of the whole array
# [start:stop:step]     # start through not past stop, by step

a = "STRINGYTHINGY"

print(a[0:3])
print(a[0:])                    # Prints complete string
print(a[:3])
print(a[:])                     # Prints complete string
print(a[1:5:2])                 
print(a[-1:-12:-2])
print(a[::-1])                  # Prints complete string in reverse since step is in reverse

a = "Pankaj"
print(a)
print(a[5])         
print(a[0:3])

"""String Methods
Python has a set of built-in methods that you can use on strings. All string methods returns new values. 
They do not change the original string.
Read more: https://www.w3schools.com/python/python_ref_string.asp
"""
print(a.isalnum())              # Asks if the string is alphanumeric, since there is no space in between, this returns true
print(a.islower())              # Returns True if all characters in the string are lower case