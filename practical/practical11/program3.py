''' 1
    3 5
    7 9 11
    13 15 17 19'''
row = int(input("Enter the row : "))

num = 1
for i in range(row):
    for j in range(i+1):
        print(num, end = " ")
        num = num+2
    print()