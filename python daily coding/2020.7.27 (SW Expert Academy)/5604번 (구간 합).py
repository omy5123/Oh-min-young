import sys
sys.stdin = open('input.txt')

"""t = int(input())

for tr in range(t):
    a, b = map(int,input().split())
    result = []
    s = 0
    for i in range(a,b+1):
        result.append(list(map(int, str(i))))
    for i in range(len(result)):
        s += sum(result[i])
    print('#%d'%(tr+1),s)"""

"""t = int(input())

for tr in range(t):
    a, b = map(int,input().split())
    result = [0]*10
    s = 0
    for i in range(a,b+1):
        arr = list(map(int, str(i)))
        for j in arr:
            result[j] += 1
    for i in range(10):
        s += (i*result[i])
    print('#%d'%(tr+1),s)
"""

t = int(input())

for tr in range(t):
    a, b = map(int,input().split())
    result = [0]*10
    point = 1
    s = 0
    while b != a and b > a:
        while (a % 10) != 0:
            for i in str(a):
                result[int(i)] += point
            a += 1
        if a > b:
            break

        while (b % 10) != 9:
            for i in str(b):
                result[int(i)] += point
            b -= 1
        if a > b:
            break
        else:
            for i in range(10):
                result[i] += ((b//10)-(a//10) + 1) * point

        point *= 10
        a //= 10
        b //= 10

    for i in range(1,10):
        s += i*result[i]
    print('#%d'%(tr+1),s)




