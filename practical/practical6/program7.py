'''
1
2   3
3   4   5
5   6   7   8
'''
row = int(input("Enter value for x: "))
for i in range(row+1):
    num=i
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()