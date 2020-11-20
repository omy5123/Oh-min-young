import sys
sys.stdin = open('input.txt')

def bfs(i,j,arr):
    global count
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = [[i, j]]
    arr[i][j] = 0
    cnt = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
                queue.append([x, y])
                arr[x][y] = 0
                cnt += 1
    if(count < cnt):
        count = cnt

n,m,k = map(int,input().split())
count = 0
arr = [[0]*m for i in range(n)]
for _ in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if(arr[i][j] == 1):
            bfs(i,j,arr)

print(count)