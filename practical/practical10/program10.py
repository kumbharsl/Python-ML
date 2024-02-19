row = int(input("Enter the char : "))

for i in range(row):
    char = 64+row
    num = row
    for j in range(row):
        print(f"{chr(char)}{num}", end=" ")
        char = char-1
        num = num-1
    print()