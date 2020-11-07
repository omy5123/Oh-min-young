import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    A,B = a,b
    while(b):
        a = a%b
        a,b = b,a
    print(A*B//a)