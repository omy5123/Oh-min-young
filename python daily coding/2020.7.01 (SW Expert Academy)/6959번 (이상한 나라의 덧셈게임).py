import sys
sys.stdin = open('input.txt')

t = int(input())
for tr in range(t):
    a = input()
    cnt = 0

    while len(a) != 1:
        x, y = a[0], a[1]
        a = str(int(x) + int(y)) + a[2:]
        cnt += 1

    if cnt % 2 == 0:
        print('#%d' %(tr+1),'B')
    else:
        print('#%d' % (tr + 1), 'A')



