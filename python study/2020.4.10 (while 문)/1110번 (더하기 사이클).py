import sys
n = int(sys.stdin.readline())
cnt = 0
update = 0
result = n
while(1):
    if(n < 10):
        update = (n*10)+n
        n = update
        cnt += 1
    else:
        update = (n%10)*10 + ((n//10+n%10)%10)
        n = update
        cnt += 1

    if (result == update):
        break
print(cnt)

