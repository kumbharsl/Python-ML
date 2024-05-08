import numpy as np

def is_armstrong(n):
    n_str = str(n)
    sum_of_cubes = sum(int(digit) ** len(n_str) for digit in n_str)
    return sum_of_cubes == n

def create_armstrong_array(rows, cols):
    arr = np.empty((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            num = i * cols + j + 1
            if is_armstrong(num):
                arr[i, j] = num
    return arr

def main():
    rows = int(input("Enter the number of rows in the array: "))
    cols = int(input("Enter the number of columns in the array: "))
    arr = create_armstrong_array(rows, cols)
    print("2D NumPy array of Armstrong numbers:")
    print(arr)
main()