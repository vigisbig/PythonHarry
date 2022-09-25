def mul(a,b,c):                     
    '''Defining a function to calculate multiplication of three numbers'''     #    This is a docstring, we use it immediately after def and 
                                                                               #    it tells the utility of function, use triple double quotes 
                                                                               #    or triple single quotes to define it.
    multiply = a*b*c
    return multiply                 # Returning the value, so that we do not get none

calc = mul(2,3,2)                   # Using variable calc to store the value of function with argument 2 
print(calc)                         # Printing the variable that uses function to calculate cube
print(mul.__doc__)                  # This is how we see the docstring, it tells us the utility of the function.
