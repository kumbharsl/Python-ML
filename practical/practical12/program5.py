row = int(input("Enter the char : "))

num=1
for i in range(row):
    for j in range(row):
        print(num, end="   ")
        num = num+1*num
    print()