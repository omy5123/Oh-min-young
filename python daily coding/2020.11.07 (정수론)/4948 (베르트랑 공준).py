import sys
sys.stdin = open('input.txt')
a = 123456
check = [0,0]+[1]*(2*a-1)
end = int((2*a)**0.5+1)
for i in range(2,end):
    if(check[i]):
        for j in range(2*i,2*a+1,i):
            check[j] = 0

while (True):
    n = int(input())
    if(n == 0):
        break
    m = 2*n
    cnt = 0
    print(sum(check[n+1:m+1]))



