i = 0

while(1):                               # This is the kind of loop that will run forever until broken, we can also use while(True).
    if (i+1<5):
        print(i, end=" ")
        i=i+1
        continue                        # Continue sends the control to start of while and after the upper if becomes false, it sends control below continue 
    print(i+1, end= " ")
    i = i+1
    if (i==44):
        break                           # We use break together with if condition to come out of while loop totally 
                                 
    