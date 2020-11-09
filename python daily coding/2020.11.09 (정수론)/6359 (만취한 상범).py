import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    n = int(input())
    check = [0, 0] + [1] * (n - 1)
    for j in range(2,n):
        for k in range(2*j,n+1,j):
            if(check[k]):
                check[k] = 0
            else:
                check[k] = 1
    print(n-sum(check[1:]))
