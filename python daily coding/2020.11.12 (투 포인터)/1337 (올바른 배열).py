import sys
sys.stdin = open('input.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

cnt = 1
ma = 1
idx_s =0

for i in range(1,n):
    cnt += 1

    while(a[i] - a[idx_s]>4):
        idx_s += 1
        cnt -= 1
    ma = max(ma,cnt)
if(ma >5):
    ma = 5
print(5-ma)