
age = int(input("Enter age: "))

if 18<age<=90:
    print("You can drive")
elif(age>90):
    print("Sit at home, you're too old to drive")
elif(age==18):
    print("We can't decide for you")
else:
    print("You must be a child")