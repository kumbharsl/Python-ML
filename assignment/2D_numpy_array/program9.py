# Write a Python program that takes a two-dimensional NumPy array
# as input from the user and prints the frequencies of each unique
# element in the array.

import numpy as np

def print_frequencies(arr):
    unique, counts = np.unique(arr, return_counts=True)
    for i in range(len(unique)):
        print("Frequency of", unique[i], ":", counts[i])

def main():
    arr = [[1,2,3],[1,2,3],[4,5,6]]
    print_frequencies(arr)

main()