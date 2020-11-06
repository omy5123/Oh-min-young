from collections import defaultdict

n = int(input())
arr=[]
brr=[]
crr=[]
drr=[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    arr.append(a)
    brr.append(b)
    crr.append(c)
    drr.append(d)

dic = defaultdict()
result = 0
for i in range(n):
    for j in range(n):
        if(arr[i] + brr[j] not in dic):
            dic[arr[i] + brr[j]] = 1
        else:
            dic[arr[i] + brr[j]] += 1

for i in range(n):
    for j in range(n):
        if(-(crr[i]+drr[j]) in dic):
            result += dic[-(crr[i]+drr[j])]

print(result)
