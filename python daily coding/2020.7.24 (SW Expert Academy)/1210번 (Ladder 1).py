import sys
sys.stdin = open('input.txt')

def bfs(i,j,arr):
    global flag
    dx = [0,0]
    dy = [-1,1]
    queue = [[i,j]]
    arr[i][j] = 0
    while queue:
        a, b = queue[0][0],queue[0][1]

        del queue[0]
        check = False
        for k in range(2):
            x = dx[k] + a
            y = dy[k] + b
            if 0<= x <100 and 0<= y < 100:
                if arr[x][y] == 1:
                    queue.append([x,y])
                    arr[x][y] = 0
                    check = True
                    break
        if not check:
            if 0 <= a+1 < 100:
                if arr[a+1][b] == 2:
                    flag = True
                    return
                queue.append([a+1,b])
                arr[a+1][b] = 0


for tr in range(10):
    n = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    copy = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            copy[i][j] = arr[i][j]

    flag = False
    for i in range(100):
        if arr[0][i] == 1:
            bfs(0,i,arr)
            if flag:
                print('#%d'%(tr+1),i)
                break
            for i in range(100):
                for j in range(100):
                    arr[i][j] = copy[i][j]