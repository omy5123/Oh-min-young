import sys
sys.stdin = open('input.txt')

def dfs(i,j,num,cnt):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if cnt == 6:
        result.append(num)
        return
    for k in range(4):
        x = dx[k] + i
        y = dy[k] + j
        if 0<= x <4 and 0<=y<4:
            dfs(x,y,num*10+arr[x][y],cnt+1)


t = int(input())

for tr in range(t):
    arr = []
    for i in range(4):
        arr.append(list(map(int, input().split())))
    cnt = 0
    result = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j],0)

    print('#%d'%(tr+1),len(set(result)))