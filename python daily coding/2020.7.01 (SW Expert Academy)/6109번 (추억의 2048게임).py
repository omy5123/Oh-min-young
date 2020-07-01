import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    a, b = input().split()
    a = int(a)
    arr = []
    for i in range(a):
        arr.append(list(map(int, input().split())))
    if b == 'up' or b == 'down':
        arr = list(map(list, zip(*arr)))
    if b == 'right' or b == 'down':
        arr = list(map(list, map(reversed, arr)))

    for i in range(a):
        if 0 in arr[i]:
            for _ in range(arr[i].count(0)):
                arr[i].remove(0)

        for j in range(1,len(arr[i])):
            if arr[i][j-1] == arr[i][j]:
                arr[i][j-1] *= 2
                arr[i][j] = 0
        for _ in range(arr[i].count(0)):
            arr[i].remove(0)

        while len(arr[i]) != a:
            arr[i].append(0)

    if b == 'right' or b == 'down':
        arr = list(map(list, map(reversed, arr)))
    if b == 'up' or b == 'down':
        arr = list(map(list, zip(*arr)))

    print('#%d'%(tr+1))
    for i in arr:
        for j in range(a):
            print(i[j], end=' ')
        print()























"""T = int(input())

for tc in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    tiles = [list(map(int, input().split())) for _ in range(N)]
    if S == 'up' or S == 'down':
        tiles = list(map(list, zip(*tiles)))
    if S == 'right' or S == 'down':
        tiles = list(map(list, map(reversed, tiles)))

    for i in range(N):
        if 0 in tiles[i]:
            for _ in range(tiles[i].count(0)):
                tiles[i].remove(0)
        cnt = 0
        for j in range(len(tiles[i]) - 1):
            if tiles[i][j] == tiles[i][j + 1]:
                tiles[i][j] *= 2
                tiles[i][j + 1] = 0
                cnt += 1
        for _ in range(cnt):
            tiles[i].remove(0)
        while len(tiles[i]) != N:
            tiles[i].append(0)

    if S == 'right' or S == 'down':
        tiles = list(map(list, map(reversed, tiles)))
    if S == 'up' or S == 'down':
        tiles = list(map(list, zip(*tiles)))
    print(f'#{tc}')
    for i in range(N):
        print(*tiles[i])"""