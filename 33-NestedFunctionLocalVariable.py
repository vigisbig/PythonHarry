# Scope of variables depends on where they are declared.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.



def myfunc():
  x = 300
  def myinnerfunc():
    print(x)              # The variable x is not available outside the function, but it is available for any function inside the function:
  myinnerfunc()

print(x)                  # This will not be printed since x is defined is local scope of myfunc() function
myfunc()