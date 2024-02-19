row = int(input("Enter the row : "))
for i in range(row):
    char = 65
    for j in range(row):
        if i % 2 == 1 :
            print(chr(char), end=" ")
            char +=1
        else:
            print(chr(char+(row-1)), end=" ")
            char -= 1
    print()