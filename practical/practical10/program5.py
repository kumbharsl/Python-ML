''' 1   2   9   4
    25  6   49  8
    81  10  121 12
    169 14  225 16'''

row = int(input("Enter the row : "))

num = 1
for i in range(row):
    for j in range(row):
        if num%2==0:
            print(num,end=" ")
        else:
            print(num*num, end=" ")
        num = num+1
    print()