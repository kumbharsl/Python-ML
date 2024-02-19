''' 1D 2C 3B 4A
    1D 2C 3B 4A
    1D 2C 3B 4A
    1D 2C 3B 4A'''
row = int(input("Enter the char : "))

for i in range(row):
    char = 64+row
    num = 1
    for j in range(row):
        print(f"{num}{chr(char)}", end=" ")
        char = char-1
        num = num+1
    print()