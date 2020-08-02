def make_matrix(A, matrix):
    dummy_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000

    return dummy_matrix

def matmul(A, B):
    if (B == 1):
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000

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
N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

result = matmul(A, B)

for row in result:
    print(*row)