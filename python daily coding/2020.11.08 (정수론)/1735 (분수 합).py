import sys
sys.stdin = open('input.txt')

a,b = map(int,input().split())
c,d = map(int,input().split())

B,D = b,d
while(d):
    b = b%d
    b,d = d,b

bunmo = B*D//b
bunza = a*(D//b) + c*(B//b)

B,D = bunza,bunmo
while(bunza):
    bunmo = bunmo%bunza
    bunmo,bunza = bunza,bunmo

print(B//bunmo,D//bunmo)