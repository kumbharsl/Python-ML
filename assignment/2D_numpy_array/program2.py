# Write a program to find the all even numbers from the given 2d numpy array
import numpy as np

def find_even_numbers(array):
    even_numbers = array[array % 2 == 0]
    return even_numbers

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
even_numbers = find_even_numbers(array)
print("Even Numbers:")
print(even_numbers)