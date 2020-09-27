import sys
sys.stdin = open('input.txt')

n = int(input())
dic = dict()
for i in range(n):
    a,b = map(str, input().split())
    if b == "leave":
        dic[a] = False
    else:
        dic[a] = True
dic = sorted(dic.items(),key = lambda x:x[0],reverse = True)
for name, check in dic:
    if check:
        print(name)