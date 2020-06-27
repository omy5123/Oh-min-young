import sys
sys.stdin = open('input.txt')

"""t = int(input())

for tr in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = []
    result = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(n-i+1):
            s = 0
            for k in range(i):
                s += arr[j+k]
            if result < s:
                result = s
    a.append(result)

for i in range(len(a)):
    print('#%d'%(i+1),a[i])"""


"""def dfs(i,result):
    for j in range(n - i + 1):
        s = 0
        for k in range(i):
            s += arr[j + k]
        if result < s:
            result = s

    if i > n:
        return result
    result = dfs(i + 1, result)

    return result


t = int(input())

for tr in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    r = []
    result = 0
    for i in range(1,n+1):
        cnt = 0
        c = dfs(i,result)
        break

    print('#%d'%(tr+1),c)"""

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_ = -10000
    sum_ = 0
    for i in range(n):
        sum_ += a[i]
        if sum_ > max_:
            max_ = sum_
        if sum_ < 0:
            sum_ = 0
    print(f"#{t+1} {max_}")
