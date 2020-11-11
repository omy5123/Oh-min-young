import sys
sys.stdin = open('input.txt')

n,k = map(int,input().split())
arr = list(map(int,input().split()))

s = 0
ma = sum(arr[:k])
result = ma
if(k == 1):
    print(max(arr))
else:
    while True:
        result -= arr[s]
        if(s >= n-k):
            break
        result += arr[s+k]
        if(ma < result):
            ma = result
        s += 1
    print(ma)
