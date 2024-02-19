''' 1
    3  2
    6  5  4
    10  9  8  7'''
row = int(input("Enter the row : " ))
num = 1
for i in range(row):
    x = num+i
    for j in range(i+1):
        print(x,end="  ")
        x -=1
    print()
    num +=(i+1)