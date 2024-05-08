# Write a Program to rotate a given 2D NumPy array by 90 degrees anti-clockwise.
# Example 1
# Input: array = np.array([[1, 2, 3],
#                          [4, 5, 6],
#                          [7, 8, 9]])

import numpy as np

def rotate_90_anticlockwise(array):
    transposed_array = np.transpose(array)
    rotated_array = np.flip(transposed_array, axis=1)
    return rotated_array

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
rotated_array = rotate_90_anticlockwise(array)
print("\nRotated Array by 90 degrees anti-clockwise:")
print(rotated_array)
