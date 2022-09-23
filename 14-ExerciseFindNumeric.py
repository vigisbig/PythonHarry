from unicodedata import numeric


l1 = [1,2,3,4,"Pankaj","Ajit","Jagmohan"]

for i in l1:
    print(type(i))

for item in l1:
    if str(item).isnumeric() and item<3:                # Using method isnumeric() method to find items in list numeric or not Using typecast since .isnumeric is a string method
        print(item)