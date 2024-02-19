'''
1   2   3   4   
1   2   3
1   2
1
'''
row = int(input("Enter value for x: "))
for i in range(row):
    num=1
    for j in range(row-i):
        print(num,end=" ")
        num+=1
    print()