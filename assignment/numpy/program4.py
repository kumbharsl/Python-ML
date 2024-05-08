# Write a Program to find the largest element in each row of a 2D NumPy array.
# Example 1
# Input: array = np.array([[1, 4, 7],
#                          [2, 5, 8],
#                          [3, 6, 9]])
# Output: [7 8 9]
import numpy as np
def largest_element_in_each_row(array):
    max_elements = np.max(array, axis=1)
    return max_elements
array = np.array([[1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9]])
largest_elements = largest_element_in_each_row(array)
print("\nLargest element in each row:")
print(largest_elements)
