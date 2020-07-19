from collections import deque

def bfs(i, j, t):
    global check
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append([i, j])
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < 100 and 0 <= y < 100:
                if arr[x][y] == 0:
                    arr[x][y] = 1
                    queue.append([x, y])
                if arr[x][y] == 3:
                    check = True
                    return check

for t in range(10):
    n = int(input())

    arr = []
    for i in range(100):
        arr.append(list(map(int, input())))

    check = False

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                bfs(i, j, t)
    if check:
        print('#%d' % (t + 1), 1)
    else:
        print('#%d' % (t + 1), 0)
