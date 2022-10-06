# No existing file here, so creating one
f = open("sample.txt","w+")
f.write("I am a good boy")
f = open("sample.txt")
print(f.readline())

# code to open file using with block below
# when we open the file using with block, we do not need to close it

with open("sample.txt") as f:
    a = f.read(4)
    print(a)

# Using old method to open and read file, compare it with block above
f = open("sample.txt")
print(f.readline())
f.close()
