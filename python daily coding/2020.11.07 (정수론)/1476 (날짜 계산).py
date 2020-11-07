import sys
sys.stdin = open('input.txt')
a,b,c,cnt = 1,1,1,1
e,s,m = map(int,input().split())

while(True):
    if(a == e and b == s and c == m):
        break
    a = a+1
    b = b+1
    c = c+1
    if(a == 16):
        a = 1
    if(b == 29):
        b = 1
    if(c == 20):
        c = 1
    cnt += 1
print(cnt)
