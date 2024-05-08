# Write a program to pad a given 2D NumPy array with zeros around its borders.
# Example 1
# Input:array = np.array([[1, 2, 3],
#                         [4, 5, 6]])
# Output:[[0 0 0 0 0]
#         [0 1 2 3 0]
#         [0 4 5 6 0]
#         [0 0 0 0 0]]

import numpy as np
def pad_with_zeros(array, pad_width):
    padded_array = np.pad(array, pad_width, mode='constant', constant_values=0)
    return padded_array
array = np.array([[1, 2, 3],
                  [4, 5, 6]])
pad_width = 1
padded_array = pad_with_zeros(array, pad_width)
print("Padded array with zeros around its borders:")
print(padded_array)
