import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

l, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))

result = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for s in range(m):
            result[i][j] += a[i][s] * b[s][j]
for i in range(n):
    for j in range(k):
        print(result[i][j],end=' ')
    print()
