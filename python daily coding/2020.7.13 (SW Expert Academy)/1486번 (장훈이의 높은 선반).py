import sys
sys.stdin = open('input.txt')

def dfs(i,s):
    if s >= b:
        result.append(s)
        return
    for j in range(i,n):
        s += arr[j]
        dfs(j+1,s)
        s -= arr[j]
    return


t = int(input())

for tr in range(t):
    n,b = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    for i in range(n):
        s = 0
        dfs(i,s)
    print('#%d'%(tr+1),min(result)-b)