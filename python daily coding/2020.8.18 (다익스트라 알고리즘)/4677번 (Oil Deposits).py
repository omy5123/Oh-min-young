import sys

from collections import deque
def bfs(i,j):
    queue = deque()
    queue.append([i, j])
    arr[i][j] = '*'
    dx = [-1,-1,-1,1,1,1,0,0]
    dy = [0,-1,1,0,-1,1,-1,1]
    while queue:
        a,b = queue.popleft()
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0<= x < m and 0<= y <n and arr[x][y] == '@':
                arr[x][y] = '*'
                queue.append([x,y])
m,n = map(int,input().split())
while m != 0:
    cnt = 0
    arr = []
    for _ in range(m):
        arr.append(list(map(str,input())))
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '@':
                bfs(i,j)
                cnt += 1
    print(cnt)
    m, n = map(int, input().split())