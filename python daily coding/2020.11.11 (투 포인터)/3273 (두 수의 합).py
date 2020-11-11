import sys
sys.stdin = open('input.txt')

n = int(input())
a = list(map(int,input().split()))
x = int(input())
a.sort()
s = 0
e = n-1
cnt = 0

while(s!= e):
    S = a[s] + a[e]
    if(S == x):
        cnt += 1
        s += 1
    elif (S > x):
        e -= 1
    else:
        s += 1

print(cnt)