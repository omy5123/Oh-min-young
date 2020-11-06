import sys
sys.stdin = open('input.txt')

m = int(input())
n = int(input())

check = [False,False] + [True]*(n-1)

for i in range(2,n+1):
    if(check[i]):
        for j in range(i*2,n+1,i):
            if(check[j]):
                check[j] = False

s = []
for i in range(m,n+1):
    if(check[i]):
        s.append(i)
if(s):
    print(sum(s))
    print(s[0])
else:
    print(-1)
