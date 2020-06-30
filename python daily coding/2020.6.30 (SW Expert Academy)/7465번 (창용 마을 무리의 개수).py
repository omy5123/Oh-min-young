import sys
sys.stdin = open('input.txt')

def dfs(i,visit,arr):
    for j in range(1,n+1):
        if visit[j] == 0 and arr[i][j] == 1:
            visit[j] = 1
            dfs(j,visit,arr)


t = int(input())

for tr in range(t):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    visit = [0]*(n+1)
    cnt = 0

    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    for i in range(1,n+1):
        if visit[i] == 0:
            dfs(i,visit,arr)
            cnt += 1

    print('#%d'%(tr+1),cnt)

