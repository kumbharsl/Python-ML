row = int(input("Enter the row : "))
for i in range(row):
    num = i*row+1
    for j in range(row):
        if num%2==1:
            print("A",end="   ")
        else:
            print(num,end="   ")
        num = num+1
    print()