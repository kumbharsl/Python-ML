import numpy as np
def altSum(arr):
    sumEle = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i + j) % 2 == 0: # Check if the sum of indices is even
                sumEle += arr[i][j]

    return sumEle
row = int(input("Enter number of rows:"))
col = int(input("Enter number of columns:"))
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print("Enter elements row-wise:")

for i in range(row):
    for j in range(col):
        arr[i][j] = int(input())
        sumEle = altSum(arr)
        print("Alternate Sum:", sumEle)