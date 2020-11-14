import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key = lambda x:(x[0]))
    m = arr[0][1]
    cnt = 0
    for j in range(1,n):
        if(m < arr[j][1]):
            cnt += 1
        else:
            m = arr[j][1]

    print(n-cnt)
