row = int(input("Enter the row : "))
num = 1
for i in range (row):
    for j in range(row):
        print (num, end=" ")
        num+=2+i
    print()
    num -=2+i