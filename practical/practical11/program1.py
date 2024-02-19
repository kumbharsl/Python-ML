''' 1
    2 2
    3 3 3
    4 4 4 4'''
row = int(input("Enter the row : "))

for i in range(row):
    num = i+1
    for j in range(i+1):
        print(num, end = " ")
    print()
