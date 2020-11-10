import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

s = 0
e = 1
mi = sys.maxsize

while(True):
    if(e>=n):
        break
    if(arr[e] - arr[s] < m):
        e += 1
        continue
    if(arr[e] - arr[s] == m):
        mi = m
        break
    mi = min(mi,arr[e]-arr[s])
    s += 1
print(mi)

