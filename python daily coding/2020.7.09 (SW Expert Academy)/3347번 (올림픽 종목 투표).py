import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [0]*n
    for i in b:
        for j in a:
            if i >= j:
                arr[a.index(j)] += 1
                break
    print('#%d' %(tr+1),arr.index(max(arr))+1)