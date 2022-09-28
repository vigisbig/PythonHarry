f = open ("newfile.txt", "w+")              # Creates a file, since a file by this name does not exist
f.write("How are you Pankaj? ")             # Writing a line in file
f.write("How are you Vinay?")               # Writing another line in file
f = open ("newfile.txt")                    # Creates a file, since a file by this name does not exist
print(f.tell())                             # Tells the position of cursor
print(f.readline())                         # Reads a line of that file
print(f.tell())                             # Tells the position of cursor
print(f.readline())                         # Reads a line of that file
print(f.tell())                             # Tells the position of cursor
f.seek(20)                                  # seek() function is used to change the position of the File Handle to a given specific position. 
# File handle is like a cursor, which defines from where the data has to be read or written in the file. 
# Syntax: f.seek(offset, from_what), where f is file pointer
# Offset: Number of positions to move forward 
# from_what: It defines point of reference.
# The reference point is selected by the from_what argument. It accepts three values: 
 # 0: sets the reference point at the beginning of the file 
 # 1: sets the reference point at the current file position 
 # 2: sets the reference point at the end of the file 
 # 0 is the default value 
print(f.tell())                             # Tells the position of cursor
print(f.readline())                         # Reads a line depending on the seek value we specified.
f.seek(0)                                   # seek() function is used to change the position of the File Handle to a given specific position. 
print(f.readline())                         # Reads a line depending on the seek value we specified.
f.close()                                   # Closing file
