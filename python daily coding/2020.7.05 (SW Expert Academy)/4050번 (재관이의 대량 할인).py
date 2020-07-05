import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)

    arr.sort()
    arr.reverse()

    result = 0
    for i in range(2,n,3):
        result += arr[i]
    print('#%d' %(tr+1),s - result)
