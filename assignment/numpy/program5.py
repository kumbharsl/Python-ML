# Write a program to find the average of each column in a 2D NumPy array.
# Example 1
# Input: array = np.array([[1, 2, 3],
#                          [4, 5, 6],
#                          [7, 8, 9]])
# Output: [4. 5. 6.]

import numpy as np
def column_averages(array):
    column_avg = np.mean(array, axis=0)
    return column_avg
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
avg_columns = column_averages(array)
print("Average of each column:")
print(avg_columns)
