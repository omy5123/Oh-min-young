n = int(input())
m = int(n**0.5)+1
i = 2

while(i <= m):
    while(n%i == 0):
        print(i)
        n //= i
    i += 1

if(n>1):
    print(n)