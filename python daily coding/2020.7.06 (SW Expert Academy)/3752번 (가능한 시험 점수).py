"""from itertools import combinations

t = int(input())

for tr in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = []
    for i in range(n+1):
        a = list(map(list,combinations(arr,i)))
        for j in a:
            if not j:
                cnt.append(0)
            if sum(j) not in cnt:
                cnt.append(sum(j))
    print('#%d' %(tr+1),len(cnt))"""


import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    arr.sort()
    a = [0]*(sum(arr)+1)
    visit = [0]
    a[0] = 1
    for i in arr:
        for j in visit[:]:
            if not a[i+j]:
                a[i+j] = 1
                visit.append(i+j)
    print('#%d' %(tr+1),sum(a))