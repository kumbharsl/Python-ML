''' 1   4   7   10
    2   5   8   11
    3   6   9   12 
    4   7   10  13'''
row = int(input("Enter the row : "))

for i in range(row):
    num = i+1
    for j in range(row):
        print(num, end=" ")
        num = num+3
    print()