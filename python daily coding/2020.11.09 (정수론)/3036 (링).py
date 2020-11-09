import sys
sys.stdin = open('input.txt')

n = int(input())

arr = list(map(int,input().split()))

for i in range(1,n):
    a,b = arr[0],arr[i]
    while(b):
        a = a%b
        a,b = b,a
    A = arr[0]//a
    B = arr[i]//a
    print(A,end='')
    print('/',end='')
    print(B)