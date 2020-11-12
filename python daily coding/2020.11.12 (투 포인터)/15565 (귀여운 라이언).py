import sys
sys.stdin = open('input.txt')

n, k = map(int,input().split())
a = list(map(int,input().split()))

s = 0
e = 0
mi = sys.maxsize
while(True):
    if(a[s:e].count(1) >= k):
        mi = min(mi, e - s)
        s += 1
    elif(e > n):
        break
    else:
        e += 1
if(mi == sys.maxsize):
    print(-1)
else:
    print(mi)