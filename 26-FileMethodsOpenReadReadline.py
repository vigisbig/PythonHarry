# Create a file by the name afile.txt and will be using it for demonstrating how file methods work
# Before you can read or write a file, you have to open it using Python's built-in open() function.

open("afile.txt")                   # open() function reads the file. Code for reading file is open(filename_extension), this will display nothing to us
f = open("afile.txt")               # creating a file object and this would be utilized to call methods associated with it.

# Syntax: object = open(file_name [, access_mode])
# file_name − Is a string value that contains the name of the file that you want to access
# access_mode − The access_mode determines the mode in which the file has to be opened, i.e. read, write, append, etc. This is optional, default is read (r) 

content = f.read()                  # Using read function to read and assigning to variable content, blank argument means read entire document
print("---1 print statement:---\n",content)
f.close()                           # Using close() method to close file. Always close file if you have opened it. For freeing resources and intended behaviour
f = open("afile.txt", "rt")         # This is same as above, even though we used "rt" method, because "rt" is default i.e read in text format             
content = f.read() 
print("--2nd print statement:---\n",content)
content = f.read(3)                 # This should have read first three letter, but it will not since it gave it all in last instance.
print("---3rd print statement:---\n", content)                             
f = open("afile.txt", "rt")         # So we repeat the entire sequence again
content = f.read(3)                 # and this time it read the three letters in 4th print statement
print("----4th print statement:----\n",content)          
f = open("afile.txt", "rb")         # This will open file in binary, since we used "b" as access mode
content = f.read()
print("----5th print statement:---\n",content)  # Gives binary output

# We can also iterate the object and read line by line like below

f = open("afile.txt", "rt")
print("----6th print statement:----")
for line in f:
    print(line, end="")
print("\n")

# We can also get output character by character by iterating content

f = open("afile.txt", "rt")
print("----7th print statement:----")
content = f.read()
for character in content:
    print(character)

# We can also get output line by line using readline method

f = open("afile.txt", "rt")
print("--8th print statement---")
print(f.readline())
print(f.readline())

# We can also get output line by line andstore as list by using readlines method

print("--9th print statement---")
f = open("afile.txt", "rt")
print(f.readlines())

# Read more: https://www.tutorialspoint.com/python/python_files_io.htm