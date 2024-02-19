''' 1  0  1  0  1
    1  0  1  0
    1  0  1
    1  0
    1'''
row = int(input("Enter the row : "))

for i in range(row):
    num = 1
    for j in range(row-i):
        if num%2==1:
            print("1",end = "  ")
        else:
            print("0",end = "  ")
        num = num+1
    print()