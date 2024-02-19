''' A   b   C
    d   E   f
    G   h   I'''

row = int(input("Enter the char : "))

num = 65
for i in range(row):
    for j in range(row):
        if num%2==1:
            print(chr(num), end=" ")
        else:
            print(chr(32+num),end = " ")
        num = num+1
    print()