import sys
sys.stdin = open('input.txt')

MOD = 1234567891
def power(x,y):
    ans = 1
    while y>0:
        if y%2 == 1:
            ans = (ans*x)%MOD
        x = (x*x)%MOD
        y //= 2

    return ans
def fac(i):
    ans = 1
    for j in range(2,i+1):
        ans = (ans*j) % MOD
    return ans

t = int(input())

for tr in range(t):
    n, r = map(int, input().split())
    result = 0
    if n == r:
        print('#%d'%(tr+1),1)
    else:
        a, b, c = fac(n), fac(r), fac(n-r)
        result = (a*power(b*c,MOD-2))%MOD
        print('#%d'%(tr+1),result)













