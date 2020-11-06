import sys


n,k = map(int,input().split())

check = [False]*(n+1)
cnt = 0
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if(check[j] == False):
            check[j] = True
            cnt += 1;
        else:
            continue
        if(cnt == k):
            print(j)
            sys.exit()

