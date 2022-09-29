# Scope of variables depends on where they are declared.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.


# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope (outside the function) 
# and one available in the local scope (inside the function):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()
print(x)