"""import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
cnt = 1
max = 1
result = arr[0]
for i in range(1,n):
    if (arr[i-1] == arr[i]):
        cnt += 1
    else:
        cnt = 1
    if cnt > max:
        max = cnt
        result = arr[i]
print(result)"""
import sys
from collections import Counter
sys.stdin = open('input.txt')
num = int(sys.stdin.readline())
nlist = [int(x) for x in sys.stdin.read().split()]
ndict = Counter(nlist)
m = max(ndict.values())
for i in sorted(ndict.keys()):
	if ndict[i] == m:
		print(i)
		break