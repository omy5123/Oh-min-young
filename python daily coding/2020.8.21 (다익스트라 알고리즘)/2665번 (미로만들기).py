import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i,j,arr,visit):
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
                if arr[x][y] == 1:
                    if visit[x][y] > visit[a][b]:
                        visit[x][y] = visit[a][b]
                        queue.append([x,y])
                else:
                    if visit[x][y] > visit[a][b] + 1:
                        visit[x][y] = visit[a][b] + 1
                        queue.append([x,y])

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))
inf = sys.maxsize
visit = [[inf]*n for _ in range(n)]
bfs(0,0,arr,visit)
print(visit[-1][-1])