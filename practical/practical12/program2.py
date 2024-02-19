''' A   B   C
    C   D   E
    E   F   G'''
row = int(input("Enter the char : "))

num = 65
for i in range(row):
    for j in range(row):
        print(chr(num), end=" ")
        num = num+1
    print()
    num-=1