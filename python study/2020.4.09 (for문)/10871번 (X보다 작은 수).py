import sys
n, x = map(int, sys.stdin.readline().split())
list = []
for i in range(n):
    list.extend(map(int,sys.stdin.readline().split()))
for i in range(n):
    if(list[i]<x):
        print(list[i], end = ' ')