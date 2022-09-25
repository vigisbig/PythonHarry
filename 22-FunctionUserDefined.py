a = 4
b = 8
c = sum((a,b))                    # Sum is a built-in function, but we can also create our own function using def keyword
print (c)

def cubef(c):                         
    cube = c*c*c
    return cube                   # Returning the value, so that we do not get none

calc = cubef(2)                   # Using variable calc to store the value of function with argument 2 
print(calc)                       # Printing the variable that uses function to calculate cube
