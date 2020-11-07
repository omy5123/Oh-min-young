import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
a,b = n,m
while (m !=0):
    n = n%m
    n,m = m,n
print(n)
print(a*b//n)