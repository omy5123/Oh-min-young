def make_matrix(A, matrix):
    dummy_matrix = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000000

    return dummy_matrix


def matmul(A, B):
    if (B == 1):
        for i in range(2):
            for j in range(2):
                A[i][j] %= 1000000

        return A

    elif ((B % 2) == 1):
        matrix = matmul(A, B - 1)
        new_matrix = make_matrix(A, matrix)

        return new_matrix

    else:
        matrix = matmul(A, B // 2)
        new_matrix = make_matrix(matrix, matrix)

        return new_matrix
import sys
sys.stdin = open('input.txt')

N = int(input())

A = [[1, 1], [1, 0]]
result = matmul(A, N)

print(result[0][1] % 1000000)