''' 


'''
row = int(input("Enter the row : "))

for i in range(row):
    num = 1
    for j in range(row):
        if num%2==0:
            print("=",end = " ")
        else:
            print("$",end=" ")
        num = num+1
    print()