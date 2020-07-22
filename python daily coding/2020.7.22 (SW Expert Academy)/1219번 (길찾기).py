import sys
sys.stdin = open('input.txt')

def dfs(i):
    global check
    if i == 99:
        check = True
        return

    for j in range(100):
        if visit[i][j] == 1:
            dfs(j)

for tr in range(10):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    visit = [[0]*100 for _ in range(100)]

    for i in range(0,2*m,2):
        visit[arr[i]][arr[i+1]] = 1

    check = False
    for i in range(100):
        if visit[0][i] == 1:
            dfs(i)
            break

    if check:
        print('#%d'%(tr+1),1)
    else:
        print('#%d' % (tr + 1), 0)