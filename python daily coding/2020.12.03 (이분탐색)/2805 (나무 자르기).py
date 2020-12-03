import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))

def Sum(hei):
    s = 0
    for i in a:
        if(i-hei>0):
            s += i-hei
    return s

def binary(m):
    start,end=0, max(a)
    result = 0
    while(start<=end):
        mid = (start+end)//2
        s = Sum(mid)
        if s < m:
            end = mid -1
        else:
            result = mid
            start = mid + 1

    return result

print(binary(m))

