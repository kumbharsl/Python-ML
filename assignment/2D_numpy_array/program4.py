import numpy as np
arr = [[1, 2, 3, 3, 1], 
       [2, 4, 5, 6, 1], 
       [5, 7,10, 8, 9], 
       [2, 7, 3, 5, 7],
       [2, 3, 5, 7, 9]]

print("Maximum Values in Each Row:")
for i in range(5):
    max_value = np.max(arr[i])
    print(max_value)