import sys
sys.stdin = open('input.txt')

n = int(input())

check = [0,0]+[1]*(n-1)
end = int(n**0.5)+1

sosu = []
for i in range(2,end):
    if(check[i]):
        for j in range(2*i,n+1,i):
            if(check[j]):
                check[j] = 0
for i in range(n+1):
    if(check[i]):
        sosu.append(i)

length = len(sosu)
s = 0
e = 0
cnt = 0
result = 0

while(True):
    if(result >= n):
        result -= sosu[s]
        s += 1
    elif(e == length):
        break
    else:
        result += sosu[e]
        e += 1

    if(result == n):
        cnt += 1

print(cnt)