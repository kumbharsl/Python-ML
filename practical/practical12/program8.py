row = int(input("Enter the char : "))
num = 1
for i in range(row):
    for j in range(row):
        if i%2==0:
            print(num,end = "  ")
        else:
            print(num*num,end= " ")
        num += 1
    print()