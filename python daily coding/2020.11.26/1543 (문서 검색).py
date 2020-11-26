import sys
sys.stdin = open('input.txt')

st = input()
s = input()

i = 0
cnt = 0
while (i<=len(st)):
    if(st[i:i+len(s)] == s):
        cnt += 1
        i += len(s)
    else:
        i += 1
print(cnt)


