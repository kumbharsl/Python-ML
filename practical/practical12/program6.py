
row = int(input("Enter the row : "))
for i in range(row):
    num = i+1
    for j in range(row):
        #print(num,end = " ")
        if num%2==1:
            print("$",end=" ")
        elif num == 7:
            print("=",end=" ")
        else:
            print("=", end=" ")
        num += 1
    print()