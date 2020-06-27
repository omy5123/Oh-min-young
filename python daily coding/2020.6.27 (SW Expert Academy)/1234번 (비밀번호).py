import sys
sys.stdin = open('input.txt')
for tr in range(10):
    n, m = map(str,input().split())
    arr = '0' + m
    arr = list(arr)
    while 1:
        flag = False
        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                flag = True
                arr[i-1] = 0
                arr[i] = 0
                break
        if 0 in arr:
            for i in range(2):
                arr.remove(0)
        if not flag:
            break

    arr = arr[1:]
    print('#%d' %(tr+1),end=' ')
    for i in arr:
        print(i,end='')
    print()