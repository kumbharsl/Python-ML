''' 1 2 3 4
    1 2 3
    1 2
    1'''
row = int(input("Enter the row : "))

for i in range(row):
    num = 1
    for j in range(row-i):
        print(num,end=" ")
        num=num+1
    print()