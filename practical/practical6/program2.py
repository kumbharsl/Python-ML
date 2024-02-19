'''
5   
5   4
5   4   3
5   4   3   2
5   4   3   2   1
'''
row = int(input("Enter value for x: "))
for i in range(row+1):
    num=5
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()