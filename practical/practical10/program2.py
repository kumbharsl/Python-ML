''' A   B   C
    D   E   F
    G   H   I'''
row = int(input("Enter the char : "))

num = 65
for i in range(row):
    for j in range(row):
        print(chr(char), end=" ")
        num = char+1
    print()