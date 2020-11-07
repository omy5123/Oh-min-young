import sys
sys.stdin = open('input.txt')

a = 10001
end = int(a**0.5+1)
check = [False,False]+[True]*(a-1)
for i in range(2,end):
    if(check[i]):
        for j in range(2*i,a,i):
            if(check[j]):
                check[j] = False

t = int(input())

for i in range(t):
    n = int(input())

    m = n//2
    for j in range(m, 1, -1):
        if(check[n-j] and check[j]):
            print(j,n-j)
            break