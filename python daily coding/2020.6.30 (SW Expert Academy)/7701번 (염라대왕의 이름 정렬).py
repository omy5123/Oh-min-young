import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    arr = list(set(arr))
    arr.sort()
    arr.sort(key=len)

    print('#%d' %(tr+1))
    for i in arr:
        print(i)