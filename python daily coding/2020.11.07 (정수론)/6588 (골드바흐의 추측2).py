import sys
sys.stdin = open('input.txt')

a = 1000001
end = int(a**0.5+1)
check = [False,False]+[True]*(a-1)
for i in range(2,end):
    if(check[i]):
        for j in range(2*i,a,i):
            if(check[j]):
                check[j] = False

while(True):
    n = int(input())
    if(n == 0):
        break
    boool = True
    m = n//2
    for j in range(2, m+1):
        if(check[n-j] and check[j]):
            print(n,'=',j,'+',n-j)
            boool = False
            break
    if(boool):
        print("Goldbach's conjecture is wrong.")