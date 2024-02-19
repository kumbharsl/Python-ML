'''
1
3   2
6   5   4   
10  9   8   7
'''
row = int(input("Enter value for x: "))
for i in range(row+1):
    num=1
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()