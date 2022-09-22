nu=3
count = 0
while count<nu:
    count+=1
    try:
        b = input("What is your name: ")
        a = b.upper()
        dict = {'ASHA': 12, 'BISHA': 13, 'RISHA': 19}
        print(dict[a])
        
    except KeyError:
        print("I don't understand that")
else:
    exit