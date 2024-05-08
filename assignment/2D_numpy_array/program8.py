# Write a Python program that takes a square matrix as input from the
# user and prints the sum of the elements located below the main
# diagonal.
def sum_below_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
               sum += matrix[i][j]
    return sum

def main():
    n = int(input("Enter the size of the square matrix: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input("Enter row {} elements separated by space: ".format(i+1)).split()))
        matrix.append(row)

    print("Sum of elements below the main diagonal: ", sum_below_diagonal(matrix))

main()