""" 
Operators in Python

Airthmetic Operators - Arithmetic operators are used with numeric values to perform common mathematical operations:
Assignment Operators - Assignment operators are used to assign values to variables:
Comparison Operators - Comparison operators are used to compare two values:
Logical Operators - Logical operators are used to combine conditional statements:
Identity Operators - Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Membership Operators - Membership operators are used to test if a sequence is presented in an object:
Bitwise Operators - Bitwise operators are used to compare (binary) numbers:

Read more: 
https://www.w3schools.com/python/python_operators.asp
https://www.geeksforgeeks.org/python-operators/
"""
print("--------------Airthmetic Operators---------")

print ("5+6 is", 5+6)                       # Addition
print ("5-6 is", 5-6)                       # Subtraction
print ("5*6 is", 5*6)                       # Multiplication
print ("5/6 is", 5/6)                       # Division
print ("5**3 is", 5**6)                     # Exponential
print ("10//3 is", 10//3)                   # Floor division  (Returns integer i.e. ignores values after decimal)
print ("10%3 is", 10%3)                     # Modulus  (Gives remainder, will return 0 for 5%5)

print("-----------Assignment operators------------")

x = 5                               # Assign value of right side of expression to left side operand 
print(x)
x += 5                              # Add AND: Add right-side operand with left side operand and then assign to left operand
print(x)
x -= 3                              # Subtract AND: Subtract right operand from left operand and then assign to left operand
print(x)
x *= 7                              # Multiply AND: Multiply right operand with left operand and then assign to left operand
print(x)
x /= 2                              # Divide AND: Divide left operand with right operand and then assign to left operand
print(x)
x %= 2                              # Modulus AND: Takes modulus using left and right operands and assign the result to left operand
print(x)
x = 11
x **= 2                             # Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand
print(x)
x //= 2                             # Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand
print(x)

print("------------Comparison operators------------")


x = 4
y = 9

print(x == y)                       # Checks equality
print(x != y)                       # Checks inequality
print(x < y )                       # Checks if x is smaller than y
print(x > y )                       # Checks if x is bigger than y
print(x <= y )                      # Checks if x is smaller than or equal to y
print(x >= y )                      # Checks if x is bigger than or equal to y


print("------------Logical operators------------")

a = True
b = False

print(x < 5 and  x < 10)            # Returns True if both statements are true
print(x < 5 or  x < 4)              # Returns True if one of the statements is true
print(not(x < 5 and x < 10))        # Reverses the result, returns False if the result is true
print(a and b)                      # Works like a truth table of and
print(a or b)                       # Works like a truth table of or

print("------------Identity operators------------")

a = 2
b = 3

print(a is b)
print(a is not b)

print("------------Membership operators------------")

l1 = [2,3,4,5,7,8,9,90]
print(32 in l1)
print(32 not in l1)

print("------------Bitwise operators------------")

#0 - 00
#1 - 01
#2 - 10
#3 - 11

print (0 & 2)
print (0 | 3)
