import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    result = 0

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if arr[i][j] == 1:
                for k in range(j+1,n+1):
                    if arr[k][i] == 1 and arr[j][k] == 1:
                        result += 1
    print('#%d' %(tr+1), result)


