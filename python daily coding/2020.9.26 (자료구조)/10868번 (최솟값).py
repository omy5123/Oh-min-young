"""import sys

n, m =map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(m):
    a, b = map(int,input().split())
    mi = sys.maxsize;
    for j in range(a-1,b):
        if mi >= arr[j]:
            mi = arr[j]
    print(mi)
"""
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
inf = 10 ** 9 + 7
treemin = [inf] * (2 * n + 2)
for i in range(n, 2 * n):
    treemin[i] = int(input())
for i in range(n - 1, 0, -1):
    treemin[i] = min(treemin[2 * i:2 * (i + 1)])


def query(l, r):
    resmin = inf
    resmax = -1
    while l < r:
        if l & 1:
            resmin = min(resmin, treemin[l])
            l += 1
        if r & 1:
            r -= 1
            resmin = min(resmin, treemin[r])
        l >>= 1
        r >>= 1
    return resmin


for _ in range(m):
    b, c = map(int, input().split())
    print(query(n + b - 1, n + c))