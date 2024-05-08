# WAP that takes a 2d numpy array and a threshold value as input and
# returns a new array where any element greater than the threshold is
# replaced with the threshold value
import numpy as np

def threshold_replace(arr, threshold):
    arr = threshold
    return arr
arr = [[1,2,3],[4,5,6]]
threshold = 3

arr = threshold_replace(arr, threshold)

print("Array After Replacement:")
print(arr)