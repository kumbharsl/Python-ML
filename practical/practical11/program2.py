''' 5
    5 4
    5 4 3
    5 4 3 2
    5 4 3 2 1'''
row = int(input("Enter the row : "))

for i in range(row):
    num = 5
    for j in range(i+1):
        print(num, end = " ")
        num = num-1
    print()
