# takes two 2d numpy arrays as input and returns a new
# array containing the elements that are common to both arrays
import numpy as np
def find_common_elements(arr1, arr2):
    common_elements = np.intersect1d(arr1, arr2)
    return common_elements

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[3,4,5],[6,7,8]])
common_elements = find_common_elements(arr1, arr2)

print("Common Elements:")
print(common_elements, end="")