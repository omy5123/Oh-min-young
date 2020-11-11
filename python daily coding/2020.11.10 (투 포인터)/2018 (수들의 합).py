n = int(input())

s = 1
e = 1
cnt = 0
result = 0

while(True):
    if(result >= n):
        result -= s
        s += 1
    elif(s >= n):
        break
    else:
        result += e
        e += 1

    if(result == n):
        cnt += 1
print(cnt)