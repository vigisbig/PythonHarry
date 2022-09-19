# We can either comment like this i.e using hash/pound sign - which is a line comment

'''or we can use triple quotes or triple double quotes
which enable us to use multiple paragraphs as comments
'''
# Let us see below some print statements and understand new line character \n

"""
The new line character in Python is used to mark the end of a line and the beginning of a new line. 
Knowing how to use it is essential if you want to print output to the console and work with files.
The new line character in Python is \n 

If you see this character in a string, that means that the current line ends at that point and 
a new line starts right after it.
"""

print("Hello\nWorld!")
print(f"Hello\nWorld!")


"""

By default, print statements add a new line character "behind the scenes" at the end of the string.
The default value of the end parameter of the built-in print function is \n, so a new line character is appended to the string.

"""
print("This is a line")                                 # This is basically printing "This is a line\n" Therefore the next line is in new line
print("This is another line")                           # This is printing "This is another line\n" so in both cases end = "\n" as per print function definition

print("This is a line", end="")                         # We can change the default end value i.e. \n so this ensures that the other line does not begin in new line. 
print("This is another line")                           # end is basically \n by default, and in line above, it's not, we can also use other values of end.
print("This is a line", end=",")                        # This end statement ensures that the other line does not begin in new line and has comma in between instead
print("This is another line")
print("This is a line", end=" ")                        # This end statement ensures that the other line does not begin in new line and has space in between
print("This is another line")

print("This is a line" "This is another line")          # Without comma there's no space
print("This is a line","This is another line")          # A comma provides a space

# Read more: https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines.

# Escape sequence characters

print("c:\narry")                                      # To ensure that \n is not interpreted as new line, we use an extra slash as below
print("c:\\narry")                                     # So backslash is one type of escape chracter  
print('It\'s alright')
print('Hello\tWorld')                                  # Inserts a Tab

# Read more and try here https://www.w3schools.com/python/gloss_python_escape_characters.asp