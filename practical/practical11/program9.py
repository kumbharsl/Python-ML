''' E
    E D
    E D C
    E D C B
    E D C B A'''
row = int(input("Enter the row : "))

for i in range(row):
    num = 64+row
    for j in range(i+1):
        print(chr(num),end=" ")
        num = num-1
    print()
