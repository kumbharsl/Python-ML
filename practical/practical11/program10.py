''' E F G H I
    D E F G
    C D E
    B C
    A'''
row = int(input("Enter the row : "))
for i in range(row):
    num = 64+row-i
    for i in range(row-i):
        print(chr(num),end = " ")
        num = num+1
    print()