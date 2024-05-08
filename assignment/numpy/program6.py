# Write a program to count the number of occurrences of a specific value in a 2D
# NumPy array.
# Example 1
# Input: array = np.array([[1, 2, 3],
#                          [4, 5, 6],
#                          [7, 8, 9]])
# value = 2
# Output: 1

import numpy as np
def count_occurrences(array, value):
    occurrences = np.count_nonzero(array == value)
    return occurrences
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
value = 2
occurrences = count_occurrences(array, value)
print("Number of occurrences of", value, ":", occurrences)
