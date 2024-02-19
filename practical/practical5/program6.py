row = int(input("Enter value for x: "))
for i in range(row):
    num=i+1
    for j in range(row):
        if num%2==0:
            print("@",end=" ")
        else:
            print("#",end=" ")
    print()