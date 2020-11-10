import sys
sys.stdin = open('input.txt')

n, m = map(int,input().split())
arr = list(map(int,input().split()))

s = 0
e = 0
cnt = 0
result = 0

while(True):
    if(result >= m):
        result -= arr[s]
        s += 1
    elif(e == n):
        break
    else:
        result += arr[e]
        e += 1

    if(result == m):
        cnt += 1
print(cnt)