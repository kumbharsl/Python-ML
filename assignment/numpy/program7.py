# Write a Program to find the determinant of a 2x2 matrix represented as a NumPyarray.
# Example 1
# Input: array = np.array([[1, 2],
#                          [3, 4]])
# Output: -2.0

import numpy as np
array = np.array([[1, 2],
                  [3, 4]])
determinant = array[0, 0] * array[1, 1] - array[0, 1] * array[1, 0]
print("\nDeterminant of the 2x2 matrix:", determinant)
