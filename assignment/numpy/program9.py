# Write a program to find the index of the maximum element in a 2D NumPy array.
# Example 1
# Input: array = np.array([[1, 3, 5],
#                          [4, 9, 2],
#                          [8, 7, 6]])
# Output: (1, 1)
import numpy as np
def max_element_index(array):
    flat_index = np.argmax(array)
    max_index = np.unravel_index(flat_index, array.shape)
    return max_index
array = np.array([[1, 3, 5],
                  [4, 9, 2],
                  [8, 7, 6]])
max_index = max_element_index(array)
print("Index of the maximum element:", max_index)
