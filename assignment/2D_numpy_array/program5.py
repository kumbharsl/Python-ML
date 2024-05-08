# write the program print the non-corner elements from the 2d numpy array
import numpy as np

def print_non_corner_elements(arr):
    rows, cols = arr.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            print(arr[i, j], end=' ')
        print()

# Example usage:
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13,14,15,16]])

print("\nNon-corner elements:")
print_non_corner_elements(arr)
