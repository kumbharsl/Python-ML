# Write a program to take a 2d numpy from the user and Check Whether the given
# 2D NumPy array is symmetric or not.
import numpy as np
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)
array = np.array([[1, 2, 3],
                  [4, 5, 6]])
if is_symmetric(array):
    print("The given 2D NumPy array is symmetric.")
else:
    print("The given 2D NumPy array is not symmetric.")