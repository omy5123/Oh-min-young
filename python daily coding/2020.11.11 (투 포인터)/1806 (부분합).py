import sys
n,m = map(int,input().split())
arr = list(map(int,input().split()))

s = 0
e = 0
mi = sys.maxsize
result = 0

while True:
    if(result >= m):
        result -= arr[s]
        if (e - s < mi):
            mi = e - s
        s += 1
    elif(e == n):
        break
    else:
        result += arr[e]
        e += 1

if(mi == sys.maxsize):
    print(0)
else:
    print(mi)