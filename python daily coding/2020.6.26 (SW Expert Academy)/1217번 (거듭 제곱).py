import sys
sys.stdin = open('input.txt')

def exponentiation(a,b):
    c = a**b
    return c

for tr in range (1,11):
    t = int(input())
    a, b = map(int, input().split())
    result = 0
    result = exponentiation(a,b)
    print('#%d'%(tr),result)
