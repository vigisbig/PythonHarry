# Variables - Types - Integer, Float, String and Boolean
# The kind of variable a thing is, we can use type() to detect it

var1 = 300
print(type(var1))        # Tells that its an integer

var2 = "This is text\n"
print(type(var2))        # Tells that its a string

var3 = 300.4
print(type(var3))        # Tells that its a float

var4 = True
print(type(var4))        # Tells that its a boolean

# Operations between variables

var5 = 200
var6 ="This is another text"

#a = var5 + var6         # will give error since types of these variables is different
a = var2 + var6          # Since both are strings, the strings are concatenating therefore.   
print(a)

"""What is typecasting?

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users. In this article, we will see the various technique for typecasting.

There can be two types of Type Casting in Python:

Implicit Type Casting
Explicit Type Casting

In Implicit - Python converts data type into another data type automatically. In this process, users don’t have to involve in this process.
In Explicit - In this method, Python need user involvement to convert the variable data type into certain data type in order to the operation required. 
"""
b = 68                   # b implicitly type casted to int
print(type(b))

c = str(b)               # b explicitly typecasted to string and assigned to c
print(type(c))

