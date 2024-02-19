''' 1    4   9
    16  25  36
    49  64  81'''
row = int(input("Enter the row : "))

num = 1
for i in range(row):
    for j in range(row):
        print(num*num, end=" ")
        num = num+1
    print()