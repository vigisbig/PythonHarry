# Scope of variables depends on where they are declared.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.


# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc1():
  x = 300
  print(x)
myfunc1()

print(x)        # This will not be printed since x is inside a function and it can be used only inside that function