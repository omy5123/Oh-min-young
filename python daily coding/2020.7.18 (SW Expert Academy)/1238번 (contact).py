import sys
sys.stdin = open('input.txt')

"""def dfs(m,cnt,count,result):
    visit[m] = 1
    for i in range(101):
        if visit[i] == 0 and arr[m][i] == 1:
            dfs(i,cnt+1,count,result)
    count.append(cnt)
    result.append(m)


for tr in range(10):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    arr = [[0]*101 for i in range(101)]
    for i in range(0,n,2):
        arr[a[i]][a[i+1]] = 1

    visit = [0] * (101)
    count = []
    result = []
    ind = []

    dfs(m,0,count,result)
    for i in range(len(count)):
        if count[i] == max(count):
            ind.append(i)
    s = 0
    for i in ind:
        if result[i] > s:
            s = result[i]
    print('#%d'%(tr+1),s)
"""


def dfs(x):
    for i in v[x]:
        if visit[i] > visit[x] + 1:
            visit[i] = visit[x] + 1
            dfs(i)

for tr in range(10):
    l, s = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [[] for i in range(101)]
    visit = [0xfffff] * 101
    visit[s] = 0
    for i in range(0, l, 2):
        v[arr[i]].append(arr[i + 1])
    dfs(s)
    result = s

    for i in range(101):
        if visit[i] < 0xffff and visit[result] <= visit[i]:
            result = i
    print('#%d'%(tr+1),result)