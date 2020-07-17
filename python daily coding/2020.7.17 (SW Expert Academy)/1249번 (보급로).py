from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visit[i][j] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < n and 0 <= y < n:
                if visit[x][y] == -1:
                    visit[x][y] = visit[a][b] + arr[x][y]
                    queue.append([x,y])
                else:
                    if visit[x][y] > visit[a][b] + arr[x][y]:
                        visit[x][y] = visit[a][b] + arr[x][y]
                        queue.append([x,y])
                    else:
                        continue

t = int(input())

for tr in range(t):
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(map(int,input())))
    visit = [[-1]*n for _ in range(n)]
    bfs(0,0)

    print('#%d'%(tr+1),visit[-1][-1])