''' 1
    1 2
    2 3 4
    4 5 6 7
    7 8 9 10 11'''
row = int(input("Enter the row : " ))

num = 1
for i in range(row):
    for j in range(i+1):
        print(num,end=" ")
        num +=1
    print()
    num=num-1