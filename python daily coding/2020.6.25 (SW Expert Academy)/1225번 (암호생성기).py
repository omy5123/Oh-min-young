from collections import deque

for _ in range(10):
    t = int(input())

    arr = deque(map(int, input().split()))


    while 1:
        for i in range(1,6):
            a = arr.popleft()
            if (a-i) <= 0:
                arr.append(0)
                print('#%d' %(t), end=' ')
                for j in arr:
                    print(j, end= ' ')
                print()
                break
            else:
                arr.append(a-i)
        if arr[-1] == 0:
            break
