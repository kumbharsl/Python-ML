row = int(input("Enter the char : "))

for i in range(row):
    char = 64+row
    for j in range(row):
        print(chr(char), end=" ")
        char = char-1
    print()