''' A   B   C   D
    A   B   C   D
    A   B   C   D
    A   B   C   D'''

row = int(input("Enter the row : "))
for i in range(row):
    char = 65
    for j in range(row):
        print(chr(char), end= "  ")
        char+=1
    print()
       