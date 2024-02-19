''' 1 1 1 1
    2 2 2
    3 3
    4'''
row = int(input("Enter the row : "))

for i in range(row):
    num = i+1
    for j in range(row-i):
        print(num,end=" ")
    print()