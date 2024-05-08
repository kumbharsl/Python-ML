# Write a Program to find the sum of the diagonal elements of a square 2D NumPyarray.
# Example 1
# Input: array = np.array([[1, 2, 3],
#                          [4, 5, 6],
#                          [7, 8, 9]])

import numpy as np

def diagonal_sum(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Error: Input matrix is not square.")
        return None

    diagonal_elements = np.diagonal(matrix)
    diagonal_sum = np.sum(diagonal_elements)

    return diagonal_sum
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
sum_diagonal = diagonal_sum(array)

if sum_diagonal is not None:
    print("Sum of diagonal elements:", sum_diagonal)
