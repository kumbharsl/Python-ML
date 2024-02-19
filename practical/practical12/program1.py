row = int(input("Enter the row : "))

num = 1
for i in range(row):
    for j in range(row):
        print(num*num-1,end=" ")
        num+=1
    print()
