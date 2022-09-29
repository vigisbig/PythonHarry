# Scope of variables depends on where they are declared.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.


# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)          # This will work since x is a global variable and available inside function too 

myfunc()
print(x)            # This will work as well since x is a global variable