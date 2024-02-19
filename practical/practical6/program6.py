'''
1   0   1   0   1
1   0   1   0
1   0   1
1   0
1
'''
row = int(input("Enter value for x: "))
for i in range(row):
    num=1
    for j in range(row-i):
        if num%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
        num+=1
    print()