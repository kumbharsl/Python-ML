import numpy as np
def has_duplicate_rows(array):
    row_strings = ["".join(map(str, row)) for row in array]
    counts = np.unique(row_strings, return_counts=True)[1]
    return np.any(counts > 1)
array = np.array([[1, 2, 3],
                  [2, 5, 6],
                  [7, 8, 9]])
has_duplicates = has_duplicate_rows(array)
if has_duplicates:
    print("The array contains duplicate rows.")
else:
    print("The array does not contain duplicate rows.")
