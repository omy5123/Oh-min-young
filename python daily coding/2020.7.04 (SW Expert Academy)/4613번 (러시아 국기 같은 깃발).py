import sys
sys.stdin = open('input.txt')
t = int(input())

for tr in range(t):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    a = 50*50
    for i in range(1,n-1):
        for j in range(i+1,n):
            cnt = 0
            for k in range(0,i):
                cnt += m - arr[k].count('W')
            for k in range(i,j):
                cnt += m - arr[k].count('B')
            for k in range(j,n):
                cnt += m - arr[k].count('R')
            if cnt < a:
                a = cnt
    print('#%d'%(tr+1),a)