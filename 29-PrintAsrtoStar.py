def print_star():
    r = int(input("Enter how many rows you want: "))
    fti = int(input("Enter 1 or 0: "))

    if fti == 1:
        for i in range(r):
            print("")
            for j in range(i+1):
                print("*",end ="")

    elif fti == 0:
        for i in range(r):
            print("")
            for j in range(i,r):
                print("*",end="")
    else:
        exit

    run_again()

def run_again():
    again = input("\nWant to run again (Y) or (N): ")
    if again.lower() == "y":
        print_star()
    else:
        exit
print_star()
