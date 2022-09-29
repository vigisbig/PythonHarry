# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.



# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()
print(x)

# With use the global keyword you can change a global variable from inside a function.

x = 300

def myfunc1():
  global x
  x = 200

myfunc1()
print(x)