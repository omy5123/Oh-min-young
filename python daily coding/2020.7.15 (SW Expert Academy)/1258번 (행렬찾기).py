import sys
sys.stdin = open('input.txt')

def bfs(i,j,visit,arr):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visit[i][j] = 1
    arr[i][j] = 0
    queue = []
    queue.append([i,j])
    while queue:
        a, b = queue[0][0],queue[0][1]
        del queue[0]
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x <n and 0<= y <n and visit[x][y] == 0 and arr[x][y] != 0:
                visit[x][y] = 1
                arr[x][y]= 0
                queue.append([x,y])

    ind = []
    for q in range(n):
        for p in range(n):
            if visit[q][p] != 0:
                ind.append([q,p])
    result.append([ind[-1][0]-ind[0][0]+1,ind[-1][1]-ind[0][1]+1])



t = int(input())

for tr in range(t):
    n = int(input())
    arr = []
    visit = [[0]*n for _ in range(n)]
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                bfs(i,j,visit,arr)
                visit = [[0] * n for _ in range(n)]
    result.sort(key=lambda x: x[1])
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[0] * x[1])

    print('#%d'%(tr+1),len(result),end=' ')
    for i in result:
        print(i[0],i[1],end=' ')
    print()
