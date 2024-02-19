''' 2   4   6   8
    1   3   5   7
    2   4   6   8
    1   3   5   7'''
row = int(input("Enter the char : "))

for i in range(row):
    num = i+1
    for j in range(row):
        if num%2==1:
            print(2*(j+1), end = " ")
        else:
            print(2*j+1, end=" ")
    print()