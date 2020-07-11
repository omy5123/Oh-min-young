import sys
sys.stdin = open('input.txt')

def check(i,j,arr):
    global flag
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for k in range(8):
        x = dx[k]+i
        y = dy[k]+j
        if 0 <= x < n and 0 <= y < n and arr[x][y] == '*':
            flag = not flag
            break
    if flag:
        bfs(i,j,arr)

def ch(i,j,arr):
    che = True
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for k in range(8):
        x = dx[k]+i
        y = dy[k]+j
        if 0 <= x < n and 0 <= y < n and arr[x][y] == '*':
            che = not che
            break
    return che

def bfs(i,j,arr):
    global count
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    queue = [[i,j]]
    arr[i][j] = 1
    visit[i][j] = 1
    while queue:
        cnt = 0
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        if ch(a,b,arr):
            for k in range(8):
                x = dx[k] + a
                y = dy[k] + b
                if 0 <= x < n and 0 <= y < n and arr[x][y] != '*' and visit[x][y] == 0:
                    arr[x][y] = 1
                    visit[x][y] = 1
                    queue.append([x,y])
    count += 1


t = int(input())
result = []
for tr in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))

    visit = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                flag = True
                check(i,j,arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                count += 1
    result.append('#%d %d'%(tr+1,count))
print('\n'.join(result))