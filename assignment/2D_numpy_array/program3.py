# Write a program to find the all prime numbers from the given 2d numpy array
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(array):
    prime_numbers = array[(np.vectorize(is_prime))(array)]
    return prime_numbers

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
prime_numbers = find_prime_numbers(array)
print("Prime Numbers:")
print(prime_numbers)