f = open("test.txt", "w")                               # This creates a new file, default mode is "r" i.e. read, we used "w" for writing since there's no existing file 
f.write("Pankaj is a good boy")                         # This will write into the file the text present in quotes
f = open("test.txt", "a")                               # This will open file in append mode since we have used append "a"         
a = f.write("\nPankaj can be bad at times boy")         # This will write into the file the text present in quotes, we assigned to "a" variable to see number of characters 
print(a)                                                # Printing number of characters added in the last instance
f.close()                                               # This closes the file

# r = Opens a file for reading only. 
# r+ = Opens a file for both reading and writing.
# w = Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# a = Opens a file for appending. The file pointer is at the end of the file if the file exists. 
# That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

f = open("test.txt","r+")
print(f.read())
f.write("\nThank you!")
f = open("test.txt")
print(f.read())

print("-----------------------------")

import os                                       # This is the module that let's us delete the file
f = open("new1.txt", "a+")                      # append+ mode enables to create a new file
nc = f.write("I am a good boy")                 # Since it's in append mode, the file will be appended with this statement everytime code runs
print(nc)                                       # nc will let us see the number of characters
print(f.read())                                 # reading the content and printing it
f.close()                                       # closing the file, so that we can delete it, else it will throw error
#os.remove("new1.txt")                           # removing the file using remove method